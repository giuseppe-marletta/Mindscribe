# Importazione delle librerie necessarie
from fastapi import FastAPI
from fastapi.middleware.cors import CORSMiddleware
from dotenv import load_dotenv
import os

# Carica le variabili d'ambiente dal file .env
# Questo permette di gestire in modo sicuro le chiavi API e altre configurazioni sensibili
load_dotenv()

# Inizializzazione dell'applicazione FastAPI
# Configuriamo il titolo, la descrizione e la versione dell'API
app = FastAPI(
    title="MindScribe",
    description="Un co-autore intelligente per organizzare e modificare i tuoi testi",
    version="1.0.0"
)

# Configurazione del middleware CORS (Cross-Origin Resource Sharing)
# Questo permette alle richieste di provenire da qualsiasi origine
# In un ambiente di produzione, è consigliabile limitare le origini consentite
app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # Permette richieste da qualsiasi origine
    allow_credentials=True,  # Permette l'invio di credenziali nelle richieste
    allow_methods=["*"],  # Permette tutti i metodi HTTP
    allow_headers=["*"],  # Permette tutti gli header
)

# Importazione e inclusione del router principale
# Il router contiene tutti gli endpoint dell'API
from app.routes import router
app.include_router(router)

# Punto di ingresso principale dell'applicazione
# Questo blocco viene eseguito solo quando il file viene eseguito direttamente
if __name__ == "__main__":
    import uvicorn
    # Avvia il server uvicorn con le seguenti configurazioni:
    # - host="0.0.0.0": accetta connessioni da qualsiasi indirizzo IP
    # - port=8000: utilizza la porta 8000
    # - reload=True: riavvia automaticamente il server quando il codice viene modificato
    uvicorn.run("app.main:app", host="0.0.0.0", port=8000, reload=True) 