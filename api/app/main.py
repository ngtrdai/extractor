from fastapi import FastAPI

from app.routes import extractors, extract
from starlette.middleware.cors import CORSMiddleware

app = FastAPI(
    title="Extractor API",
    description="API to extract text from PDF files",
    version="0.1.0"
)

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


@app.get('/healthcheck')
async def healthcheck():
    return {"status": "ok"}


app.include_router(extractors.router)
app.include_router(extract.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
