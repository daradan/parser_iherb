from pydantic import BaseModel
from typing import Optional


class ProductSchema(BaseModel):
    store_id: str
    name: str
    category: str
    url: str
    brand: str
    images: str
    rating: str
    rating_count: str
    rating_url: str
    review_url: str


class PriceSchema(BaseModel):
    price: str
    product_id: Optional[int]
    discount: str = '0'
