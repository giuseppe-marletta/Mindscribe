from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Carica le variabili d'ambiente
load_dotenv()

# Inizializza l'app FastAPI
app = FastAPI(
    title="MindScribe",
    description="Un co-autore intelligente per organizzare e modificare i tuoi testi",
    version="1.0.0"
)

# Configura CORS
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Importa le routes
from app.routes import router
app.include_router(router)

if __name__ == "__main__":
    import uvicorn
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True) 