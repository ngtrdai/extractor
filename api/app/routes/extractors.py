from http.client import HTTPException
from typing import List

from fastapi import APIRouter, Depends
from app.schemas.extractor_schema import StoreExtractor, ExtractorResponse
from sqlalchemy.orm import Session
from app.database import get_session
from app.models.extractor import Extractor

router = APIRouter(
    prefix="/extractors",
    tags=["extractors"],
    responses={404: {"description": "Not found"}},
)


@router.get("")
async def index(
        session: Session = Depends(get_session)
) -> List[ExtractorResponse]:
    extractors = (session.query(Extractor).order_by(Extractor.created_at.desc()).all())

    return [
        ExtractorResponse(
            uuid=extractor.uuid,
            name=extractor.name,
            description=extractor.description,
            prompt=extractor.prompt,
            schema=extractor.schema,
            created_at=extractor.created_at
        )
        for extractor in extractors
    ]


@router.post("")
async def store(
        request: StoreExtractor,
        session: Session = Depends(get_session)
) -> ExtractorResponse:
    extractor = Extractor(
        name=request.name,
        description=request.description,
        prompt=request.prompt,
        schema=request.json_schema
    )
    session.add(extractor)
    session.commit()

    return ExtractorResponse(
        uuid=extractor.uuid,
        name=extractor.name,
        description=extractor.description,
        prompt=extractor.prompt,
        schema=extractor.schema
    )


@router.get("/{uuid}")
async def show(
        uuid: str,
        session: Session = Depends(get_session)
) -> ExtractorResponse:
    extractor = session.query(Extractor).filter_by(uuid=uuid).first()

    return ExtractorResponse(
        uuid=extractor.uuid,
        name=extractor.name,
        description=extractor.description,
        prompt=extractor.prompt,
        schema=extractor.schema
    )


@router.put("/{uuid}")
async def update(
        uuid: str,
        request: StoreExtractor,
        session: Session = Depends(get_session)
) -> ExtractorResponse:
    extractor = session.query(Extractor).filter_by(uuid=uuid).first()

    extractor.name = request.name
    extractor.description = request.description
    extractor.prompt = request.prompt
    extractor.schema = request.json_schema

    session.commit()

    return ExtractorResponse(
        uuid=extractor.uuid,
        name=extractor.name,
        description=extractor.description,
        prompt=extractor.prompt,
        schema=extractor.schema
    )


@router.delete("/{uuid}")
async def delete(
        uuid: str,
        session: Session = Depends(get_session)
) -> None:
    extractor = session.query(Extractor).filter_by(uuid=uuid).first()

    if not extractor:
        raise HTTPException("Extractor not found")

    session.delete(extractor)
    session.commit()
