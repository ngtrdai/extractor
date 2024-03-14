from datetime import datetime
from typing import Dict, Any
from uuid import UUID
from pydantic import BaseModel, Field, validator
from app.ultils.validators import validate_json_schema


class StoreExtractor(BaseModel):
    name: str = Field(default="", description="Name of the extractor")
    description: str = Field(default="", description="Description of the extractor")
    json_schema: Dict[str, Any] = Field(
        ...,
        description="The schema of the extractor",
        alias="schema"
    )
    prompt: str = Field(
        ...,
        description="The prompt for the extractor"
    )

    @validator("json_schema")
    def validate_schema(cls, value: Dict[str, Any]) -> Dict[str, Any]:
        validate_json_schema(value)
        return value


class ExtractorResponse(BaseModel):
    uuid: UUID
    name: str
    description: str
    prompt: str
    json_schema: Dict[str, Any] = Field(
        ...,
        description="The schema of the extractor",
        alias="schema"
    )
    created_at: datetime = Field(
        default=None,
        description="The creation date and time of the extractor"
    )
