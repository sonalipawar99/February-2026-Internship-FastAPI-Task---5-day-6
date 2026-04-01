from fastapi import FastAPI
from typing import List
from pydantic import BaseModel

app = FastAPI()

# Sample data
products = [
    {"id": 1, "name": "Wireless Mouse", "price": 499, "category": "Electronics"},
    {"id": 2, "name": "Notebook", "price": 99, "category": "Stationery"},
    {"id": 3, "name": "USB Hub", "price": 799, "category": "Electronics"},
    {"id": 4, "name": "Pen Set", "price": 49, "category": "Stationery"},
]

orders = []

class Order(BaseModel):
    order_id: int
    customer_name: str
    items: List[int]  # product IDs

@app.get("/products")
def get_products():
    return products

@app.post("/orders")
def create_order(order: Order):
    orders.append(order.dict())
    return {"message": "Order created", "order": order.dict()}