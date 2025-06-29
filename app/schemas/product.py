from pydantic import BaseModel
from typing import Optional

# Category schemas
class CategoryBase(BaseModel):
    name: str

class CategoryCreate(CategoryBase):
    pass

class CategoryOut(CategoryBase):
    id: int

    class Config:
        orm_mode = True

# Product schemas
class ProductBase(BaseModel):
    name: str
    price: float
    discount: Optional[float] = 0
    image: Optional[str] = None
    in_stock: Optional[bool] = True
    description: Optional[str] = None
    category_id: int

class ProductCreate(ProductBase):
    pass

class ProductOut(ProductBase):
    id: int
    category: CategoryOut

    class Config:
        orm_mode = True
