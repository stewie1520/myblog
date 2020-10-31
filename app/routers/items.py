from fastapi import APIRouter, Path, Body
from typing import List, Optional
from pydantic import BaseModel, Field

router = APIRouter()


class Item(BaseModel):
    name: str
    description: Optional[str] = Field(None,
        title="The description of the item", max_length=300)
    price: float = Field(..., gt=0, description="The price must be greater than zero")
    tax: Optional[float] = None


class User(BaseModel):
    username: str
    full_name: Optional[str] = None


@router.put("/{item_id}")
async def update_item(
    *,
    item_id: int = Path(..., title="The ID of the item to get", ge=0, le=1000),
    item: Item = Body(..., embed=True),
):
    pass
