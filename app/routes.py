# Importazione delle librerie e moduli necessari
from fastapi import APIRouter, HTTPException
from pydantic import BaseModel
from typing import Optional
from app.agents.organizer import organize_text
from app.agents.editor import edit_text
from app.utils.io import save_to_file
from app.utils.logger import log_interaction

# Creazione del router principale
router = APIRouter()

# Definizione dei modelli di dati per la validazione degli input
class TextInput(BaseModel):
    """Modello per l'input del testo da organizzare."""
    content: str  # Il contenuto testuale da elaborare
    style: Optional[str] = None  # Stile opzionale per la formattazione

class EditRequest(BaseModel):
    """Modello per le richieste di modifica del testo."""
    content: str  # Il testo da modificare
    instruction: str  # L'istruzione per la modifica (es. "rendi più formale")

class ExportRequest(BaseModel):
    """Modello per le richieste di esportazione."""
    content: str  # Il contenuto da esportare
    format: str  # Il formato di esportazione (solo "markdown")

# Endpoint per l'organizzazione del testo
@router.post("/organize")
async def organize_endpoint(input_data: TextInput):
    """
    Endpoint per organizzare il testo in input in una struttura logica.
    
    Args:
        input_data (TextInput): Il testo da organizzare
        
    Returns:
        dict: Dizionario contenente il testo organizzato
        
    Raises:
        HTTPException: Se si verifica un errore durante l'elaborazione
    """
    try:
        # Chiamata all'agente organizzatore
        organized_text = await organize_text(input_data.content)
        # Log dell'interazione
        log_interaction("organize", input_data.content, organized_text)
        return {"organized_text": organized_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint per la modifica del testo
@router.post("/edit")
async def edit_endpoint(edit_request: EditRequest):
    """
    Endpoint per modificare il testo secondo le istruzioni fornite.
    
    Args:
        edit_request (EditRequest): La richiesta di modifica contenente il testo e l'istruzione
        
    Returns:
        dict: Dizionario contenente il testo modificato
        
    Raises:
        HTTPException: Se si verifica un errore durante l'elaborazione
    """
    try:
        # Chiamata all'agente editor
        edited_text = await edit_text(edit_request.content, edit_request.instruction)
        # Log dell'interazione
        log_interaction("edit", edit_request.content, edited_text, edit_request.instruction)
        return {"edited_text": edited_text}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e))

# Endpoint per l'esportazione del testo
@router.post("/export")
async def export_endpoint(export_request: ExportRequest):
    """
    Endpoint per esportare il testo nel formato specificato (solo markdown).
    
    Args:
        export_request (ExportRequest): La richiesta di esportazione contenente il testo e il formato
        
    Returns:
        dict: Dizionario contenente il percorso del file esportato
        
    Raises:
        HTTPException: Se si verifica un errore durante l'esportazione
    """
    try:
        # Salvataggio del file nel formato richiesto
        file_path = await save_to_file(export_request.content, export_request.format)
        return {"file_path": file_path}
    except Exception as e:
        raise HTTPException(status_code=500, detail=str(e)) 