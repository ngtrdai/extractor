from typing import Generator

from sqlalchemy import create_engine
from sqlalchemy.orm import Session, sessionmaker

from app.settings import get_database_url

ENGINE = create_engine(get_database_url())
SessionClass = sessionmaker(bind=ENGINE)


def get_session() -> Generator[Session, None, None]:
    session = SessionClass()

    try:
        yield session
    except Exception:
        session.rollback()
        raise
    finally:
        session.close()
