import os

from langchain_openai import ChatOpenAI
from sqlalchemy.engine import URL


GPT_MODEL_NAME = "gpt-3.5-turbo"


def get_database_url() -> URL:
    return URL.create(
        drivername='postgresql',
        username=os.environ['DB_USER'],
        password=os.environ['DB_PASSWORD'],
        host='database',
        database=os.environ['DB_NAME'],
        port=5432
    )


def get_gpt_model() -> ChatOpenAI:
    return ChatOpenAI(model=GPT_MODEL_NAME, temperature=0)
