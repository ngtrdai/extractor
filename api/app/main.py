from fastapi import FastAPI

from app.routes import extractors

app = FastAPI(
    title="PDF Extractor API",
    description="API to extract text from PDF files",
    version="0.1.0"
)


@app.get('/healthcheck')
async def healthcheck():
    return {"status": "ok"}


app.include_router(extractors.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
