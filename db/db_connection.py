import os
from pymongo import MongoClient
from functools import lru_cache
import config

@lru_cache
def get_settings():
    return config.Settings()

def get_database(dbName: str):
    # Obtener la cadena de conexión desde la variable de entorno
    CONNECTION_STRING = get_settings().mongo_uri

    if not CONNECTION_STRING:
        raise ValueError("No se encontró la variable de entorno MONGO_URI")

    client = MongoClient(CONNECTION_STRING)
    return client[dbName]