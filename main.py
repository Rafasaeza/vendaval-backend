from fastapi import FastAPI
from routers import articulos_router, pujas_router
from fastapi.middleware.cors import CORSMiddleware
from db_connection import get_database
import os

app = FastAPI()
db = get_database("vendaval")
dqe
#Añadir CORS
origins = [
    "https://vendaval-frontend.vercel.app",
    "http://localhost:3000",  # Origen permitido
    # Añade otros orígenes si es necesario
]

app.add_middleware(
    CORSMiddleware,
    allow_origins=origins,
    allow_origin_regex=r"https://.*\.vercel\.app",
    allow_credentials=True,
    allow_methods=["*"],  # Permitir todos los métodos HTTP (GET, POST, etc.)
    allow_headers=["*"],  # Permitir todos los encabezados
)

app.include_router(articulos_router.router, prefix="/articulos", tags=["Artículos"])
app.include_router(pujas_router.router, prefix="/pujas", tags=["Pujas"])

