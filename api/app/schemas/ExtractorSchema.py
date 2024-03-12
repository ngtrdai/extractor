from pydantic import BaseModel, Field


class CreateExtractor(BaseModel):
    name: str = Field(default="", description="Name of the extractor")
    description: str = Field(default="", description="Description of the extractor")
