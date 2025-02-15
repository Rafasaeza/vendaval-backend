# base_model/puja.py
from pydantic import BaseModel, EmailStr
from datetime import datetime

class Puja(BaseModel):
    articulo_id: str
    comprador: EmailStr
    timestamp: datetime
    cantidad: int

