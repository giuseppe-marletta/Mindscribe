# Importazione delle librerie necessarie
import os
import markdown2
import pdfkit
from datetime import datetime

async def save_to_file(content: str, format: str) -> str:
    """
    Salva il contenuto in un file nel formato specificato (solo markdown).
    
    Args:
        content (str): Il contenuto da salvare
        format (str): Il formato di output (solo "markdown")
        
    Returns:
        str: Il percorso del file salvato
        
    Raises:
        ValueError: Se il formato specificato non è supportato
        Exception: Se si verifica un errore durante il salvataggio
        
    Note:
        I file vengono salvati nella cartella output/ con timestamp
    """
    # Creazione della directory per i file di output se non esiste
    os.makedirs("output", exist_ok=True)
    
    # Generazione del timestamp per il nome file
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if format.lower() == "markdown":
        # Salvataggio in formato Markdown
        file_path = f"output/document_{timestamp}.md"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return file_path
    else:
        # Gestione del formato non supportato
        raise ValueError(f"Formato non supportato: {format}") 