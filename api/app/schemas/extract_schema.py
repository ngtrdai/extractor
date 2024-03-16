from typing import List, Any, Dict

from pydantic import BaseModel, Field


class ExtractRequest(BaseModel):
    text: str = Field(..., description="The text to be extracted")
    json_schema: Dict[str, Any] = Field(
        ...,
        description="The schema of the extractor",
        alias="schema"
    )
    prompt: str = Field(
        ...,
        description="The prompt for the extractor"
    )


class ExtractResponse(BaseModel):
    data: List[Any]
