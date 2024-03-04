from fastapi import APIRouter

router = APIRouter(
    prefix="/extractors",
    tags=["extractors"],
    responses={404: {"description": "Not found"}},
)


@router.get("/")
async def read_root():
    return {"message": "Welcome to the PDF Extractor API!"}