from app.models.base_model import TimestampMixin
from sqlalchemy import Column, String, Text
from sqlalchemy.dialects.postgresql import JSONB


class Extractor(TimestampMixin):
    __tablename__ = "extractors"

    name = Column(
        String(255),
        server_default="",
        nullable=False,
    )
    description = Column(
        String(255),
        server_default="",
        nullable=False,
    )
    prompt = Column(
        Text,
        nullable=False
    )
    schema = Column(
        JSONB,
        nullable=False
    )

    def __repr__(self):
        return f"<Extractor(name={self.name}, description={self.description})>"
