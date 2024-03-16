from app.models.extractor import Extractor
from langchain.chains.structured_output import create_openai_fn_runnable
from langchain_core.prompts import ChatPromptTemplate
from langchain_core.runnables import chain
from langchain_text_splitters import TokenTextSplitter
from app.settings import GPT_MODEL_NAME
from app.schemas.extract_schema import ExtractRequest
from app.ultils.parser import convert_schema_to_openai_format
from app.settings import get_gpt_model


def make_prompt(prompt: str, func_name: str):
    prompt_prefix = (
        "You are a top-tier algorithm for extracting information from text. "
        "Only extract information that is relevant to the provided text. "
        "If no information is relevant, use the schema and output "
        "an empty list where appropriate."
    )

    if prompt:
        sys_message = ("system", f"{prompt_prefix}\n\n{prompt}")
    else:
        sys_message = ("system", prompt_prefix)
    prompt_components = [sys_message, (
        "human",
        "I need to extract information from "
        "the following text: ```\n{text}\n```\n",
    )]

    return ChatPromptTemplate.from_messages(prompt_components)


@chain
async def runnable(requests: ExtractRequest):
    openapi_func = convert_schema_to_openai_format(requests.json_schema)
    func_name = openapi_func["name"]
    prompt = make_prompt(requests.prompt, func_name)
    return await create_openai_fn_runnable(
        functions=[openapi_func], llm=get_gpt_model(), prompt=prompt
    ).ainvoke({"text": requests.text})


class Extract:
    raw: str
    extractor: Extractor

    def __init__(self, raw: str, extractor: Extractor):
        self.raw = raw
        self.extractor = extractor

    async def extract(self):
        json_schema = self.extractor.schema
        splitter = TokenTextSplitter(
            chunk_size=int(4096 * 0.8),
            chunk_overlap=20,
            model_name=GPT_MODEL_NAME
        )
        texts = splitter.split_text(self.raw)
        requests = [
            ExtractRequest(
                text=text,
                schema=json_schema,
                prompt=self.extractor.prompt
            )
            for text in texts
        ]

        return await runnable.abatch(requests, {"max_concurrency": 1})

    async def generate(self):
        return await self.extract()
