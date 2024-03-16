from typing import Annotated, Optional
from uuid import UUID
from fastapi import APIRouter, Form, File, UploadFile, HTTPException, Depends
from sqlalchemy.orm import Session
from app.database import get_session
from app.models.extractor import Extractor
from app.ultils.parser import parse_file_to_document

from app.extract import Extract

router = APIRouter(
    prefix="/extract",
    tags=["extract"],
    responses={404: {"description": "Not found"}},
)


@router.post("")
async def extract(
        extractor_uuid: Annotated[UUID, Form()],
        text: Optional[str] = Form(None),
        file: Optional[UploadFile] = File(None),
        session: Session = Depends(get_session)
):
    if text is None and file is None:
        raise HTTPException(status_code=422, detail="Either text or file must be provided")

    extractor = session.query(Extractor).filter(Extractor.uuid == extractor_uuid).first()

    if extractor is None:
        raise HTTPException(status_code=404, detail="Extractor not found")

    if text:
        _text = text
    else:
        _text = "\n".join([document.page_content for document in parse_file_to_document(file.file)])

    extracted = await Extract(_text, extractor).generate()
    return {
        "text": extracted
    }
