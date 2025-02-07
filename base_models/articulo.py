# base_model/articulo.py
from pydantic import BaseModel, EmailStr
from typing import List, Optional

class Articulo(BaseModel):
    vendedor: EmailStr
    descripcion: str
    precio_salida: int
    imagenes: List[str]
    comprador: Optional[EmailStr] = None
