from fastapi import FastAPI

from app.routes import extractors, extract

app = FastAPI(
    title="PDF Extractor API",
    description="API to extract text from PDF files",
    version="0.1.0"
)


@app.get('/healthcheck')
async def healthcheck():
    return {"status": "ok"}


app.include_router(extractors.router)
app.include_router(extract.router)


if __name__ == "__main__":
    import uvicorn
    uvicorn.run(app, host="localhost", port=8000)
