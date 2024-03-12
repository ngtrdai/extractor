from fastapi import APIRouter, Depends

from app.schemas.ExtractorSchema import CreateExtractor
from sqlalchemy.orm import Session

from app.database import get_session

from app.models.Extractor import Extractor

router = APIRouter(
    prefix="/extractors",
    tags=["extractors"],
    responses={404: {"description": "Not found"}},
)


@router.post("")
async def store(
        request: CreateExtractor,
        session: Session = Depends(get_session)
) -> dict:
    extractor = Extractor(
        name=request.name,
        description=request.description,
        prompt=request.prompt,
        schema=request.schema
    )
    session.add(extractor)
    session.commit()

    return {
        "id": extractor.id,
        "name": extractor.name,
        "description": extractor.description,
        "prompt": extractor.prompt,
        "schema": extractor.schema
    }


@router.get("")
async def index(
        session: Session = Depends(get_session)
) -> list:
    extractors = session.query(Extractor).all()

    return [
        {
            "uuid": extractor.uuid,
            "name": extractor.name,
            "description": extractor.description,
            "prompt": extractor.prompt,
            "schema": extractor.schema
        }
        for extractor in extractors
    ]
