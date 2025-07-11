from typing import Optional

from fastapi import APIRouter, HTTPException
from full_app_structure.models.item import Item
from full_app_structure.response.basic_response import BasicResponse
from full_app_structure.services.item_service import get_item_by_id
from full_app_structure.services.products_service import fetch_all_products

router = APIRouter()

@router.get("/read/{item_id}", response_model=Item)
def read_item(item_id: int) -> BasicResponse:
    """ Read an item by ID """
    item : get_item_by_id(item_id) | None
    return {
        None: BasicResponse(None, 404, "Item not found"),
    }.get(item, BasicResponse(item, 200))

# @router.get("/all", response_description="Products list")
# def fetch_all_products_list():
#     item = fetch_all_products()
#     print(item)
#     if not item:
#         raise HTTPException(status_code=404, detail="Item not found")
#     return item

@router.get("/all", response_description="Products list")
def fetch_all_products_list():
    item = fetch_all_products()
    print(item)
    if not item:
        raise HTTPException(status_code=404, detail="Item not found")
    return item