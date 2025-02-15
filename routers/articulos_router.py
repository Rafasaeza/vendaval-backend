# routers/articulos.py
from fastapi import APIRouter, HTTPException, Query
from db_connection import get_database
from schemas.articulo import Articulo
from typing import List
from bson.objectid import ObjectId
from pydantic import BaseModel
router = APIRouter()

def get_collection():
    db = get_database("vendaval")
    return db.get_collection("articulos")

@router.post("/", status_code=201)
def crear_articulo(articulo: Articulo):
    collection = get_collection()
    result = collection.insert_one(articulo.dict())
    return {"id": str(result.inserted_id)}

@router.get("/{articulo_id}")
def obtener_articulo(articulo_id: str):
    collection = get_collection()
    articulo = collection.find_one({"_id": articulo_id})
    if not articulo:
        raise HTTPException(status_code=404, detail="Artículo no encontrado")
    return articulo

@router.get("/")
def obtener_articulos(
    query: str = Query(None, title="Filtro por descripción"),
    vendedor: str = Query(None, title="Filtro por vendedor")
):
    collection = get_collection()

    filtro = {}
    if query:
        filtro["descripcion"] = {"$regex": query, "$options": "i"}
    if vendedor:
        filtro["vendedor"] = vendedor  # Filtrar por el vendedor específico

    articulos = list(collection.find(filtro))
    
    if not articulos:
        raise HTTPException(status_code=404, detail="No se encontraron artículos con esos filtros")

    # Convertir ObjectId a string
    for articulo in articulos:
        articulo["_id"] = str(articulo["_id"])

    return articulos

class AdjudicacionRequest(BaseModel):
    comprador: str

@router.put("/adjudicar/{articulo_id}")
def adjudicar_articulo(articulo_id: str, request: AdjudicacionRequest):
    collection = get_collection()

    # Verificar si el artículo existe
    articulo = collection.find_one({"_id": ObjectId(articulo_id)})
    if not articulo:
        raise HTTPException(status_code=404, detail="Artículo no encontrado")

    # Actualizar el artículo con el comprador adjudicado
    result = collection.update_one(
        {"_id": ObjectId(articulo_id)},
        {"$set": {"comprador": request.comprador}}
    )

    if result.modified_count == 0:
        raise HTTPException(status_code=400, detail="No se pudo adjudicar el artículo")

    return {"message": "Artículo adjudicado con éxito"}