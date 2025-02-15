import os
from pymongo import MongoClient
from dotenv import load_dotenv

load_dotenv()

def get_database(dbName: str):
    # Obtener la cadena de conexión desde la variable de entorno
    CONNECTION_STRING = os.getenv("MONGO_URI")

    if not CONNECTION_STRING:
        raise ValueError("No se encontró la variable de entorno MONGO_URI")

    client = MongoClient(CONNECTION_STRING)
    return client[dbName]