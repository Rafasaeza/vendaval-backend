from fastapi import FastAPI
from endpoints import articulos
from endpoints import pujas
from fastapi.middleware.cors import CORSMiddleware
from db.db_connection import get_database
from functools import lru_cache
import config
app = FastAPI()
db = get_database("vendaval")

@lru_cache
def get_settings():
    return config.Settings()

app.add_middleware(
    CORSMiddleware,
    allow_origins=[get_settings().allowed_origin],
    #allow_origin_regex=origins,#r"https://.*\.vercel\.app",
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

app.include_router(articulos.router, prefix="/articulos", tags=["Artículos"])
app.include_router(pujas.router, prefix="/pujas", tags=["Pujas"])

