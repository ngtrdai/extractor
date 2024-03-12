from typing import BinaryIO, List

from langchain.document_loaders.parsers import PDFMinerParser
from langchain.document_loaders.parsers.generic import MimeTypeBasedParser
from langchain_community.document_loaders import Blob
from langchain_core.documents import Document


HANDLED_MIME_TYPES = {
    "application/pdf": PDFMinerParser()
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
