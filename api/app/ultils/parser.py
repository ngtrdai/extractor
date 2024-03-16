from typing import BinaryIO, List, Union

from langchain.document_loaders.parsers import PDFMinerParser
from langchain.document_loaders.parsers.generic import MimeTypeBasedParser
from langchain_community.document_loaders import Blob
from langchain_core.documents import Document
from langchain_core.utils.json_schema import dereference_refs

HANDLED_MIME_TYPES = {
    "application/pdf": PDFMinerParser()
}


def remove_title(schema: dict) -> dict:
    new_schema = {}
    for key, value in schema.items():
        if key == "title":
            continue
        elif isinstance(value, dict):
            new_schema[key] = remove_title(value)
        else:
            new_schema[key] = value

    return new_schema


def convert_schema_to_openai_format(
        schema: Union[dict, list]
):
    if isinstance(schema, dict):
        _schema = dereference_refs(schema)
    else:
        _schema = {
            "anyOf": [dereference_refs(s) for s in schema]
        }

    return {
        "name": "query",
        "description": "The query to be executed",
        "parameters": remove_title({
            "type": "object",
            "properties": {
                "data": {
                    "type": "array",
                    "items": _schema
                }
            },
            "required": ["data"]
        })
    }


def convert_binary_to_blob(file: BinaryIO) -> Blob:
    file_content = file.read()
    mine_type = "application/pdf"
    file_name = "Test"
    return Blob.from_data(
        data=file_content,
        mime_type=mine_type,
        path=file_name
    )


def parse_file_to_document(file: BinaryIO) -> List[Document]:
    return MimeTypeBasedParser(
        HANDLED_MIME_TYPES,
        fallback_parser=None
    ).parse(convert_binary_to_blob(file))
