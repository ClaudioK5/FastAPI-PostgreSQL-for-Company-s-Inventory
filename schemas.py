from pydantic import BaseModel


class InventoryItemCreate(BaseModel):

    name: str
    quantity: int
    price: float

class InventoryItem(BaseModel):

    id: int
    name: str
    quantity: int
    price: float

    class Config:

        orm_mode = True