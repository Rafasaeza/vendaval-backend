# routers/pujas.py
from fastapi import APIRouter, HTTPException, Depends
from db_connection import get_database
from base_models.puja import Puja

router = APIRouter()

def get_collection():
    db = get_database("vendaval")
    return db.get_collection("pujas")


@router.post("/")
def realizar_puja(puja: Puja):
    collection = get_collection()

    # Obtener la última puja más alta para el artículo
    ultima_puja = collection.find_one(
        {"articulo_id": puja.articulo_id}, 
        sort=[("cantidad", -1)]  # Orden descendente por cantidad
    )

    # Validar que la nueva puja sea mayor a la última puja
    if ultima_puja and puja.cantidad <= ultima_puja["cantidad"]:
        raise HTTPException(
            status_code=400, 
            detail=f"La puja debe ser mayor a {ultima_puja['cantidad']}"
        )

    # Insertar la nueva puja
    result = collection.insert_one(puja.dict())
    return {"id": str(result.inserted_id)}

@router.get("/{articulo_id}")
def obtener_pujas(articulo_id: str):
    collection = get_collection()
    pujas = list(collection.find({"articulo_id": articulo_id}))
    return pujas

@router.get("/max/{articulo_id}")
def obtener_puja_maxima(articulo_id: str):
    collection = get_collection()

    # Buscar la puja con mayor cantidad para el artículo
    puja_maxima = collection.find_one(
        {"articulo_id": articulo_id},
        sort=[("cantidad", -1)]  # Orden descendente por cantidad
    )

    if not puja_maxima:
        return {"cantidad": 0, "comprador": None}

    return {"cantidad": puja_maxima["cantidad"], "comprador": puja_maxima["comprador"]}
