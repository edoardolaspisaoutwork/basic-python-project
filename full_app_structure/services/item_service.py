from typing import Optional

from full_app_structure.models.item import Item

# Dummy data
ITEMS = {
    1: {"id": 1, "name": "Keyboard", "description": "Mechanical keyboard"},
    2: {"id": 2, "name": "Mouse", "description": "Wireless mouse"}
}

def get_item_by_id(item_id: int) -> Optional[Item]:
    data = ITEMS.get(item_id)
    return Item(**data) if data else None

def executeQuery():
    with connection_pool.connection() as conn:
        return conn.execute("SELECT * FROM products").fetchall()