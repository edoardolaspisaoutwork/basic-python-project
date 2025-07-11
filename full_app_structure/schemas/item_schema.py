from typing import Optional

from pydantic import BaseModel, Field
import uuid


class Item(BaseModel):
    id: uuid.UUID = Field(description="The unique ID of the item", default_factory=uuid.uuid4)
    name: str = Field(description="The name of the item", examples=["Item", "Meti"])
    description: Optional[str] = Field(description="The description of the item", examples=["This is a good item"])

    class Config:
        schema_extra = {
            "example": {
                "id": "71cb2019-34c3-45b6-93d7-afbc76803692",
                "name": "Item",
                "description": "This is a good item"
            }
        }