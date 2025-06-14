# Importazione delle librerie necessarie
import os
import json
from datetime import datetime
from loguru import logger

# Configurazione del logger principale
# Il logger salva i file nella cartella prompts_logs con rotazione automatica
logger.add(
    "prompts_logs/mindscribe_{time}.log",  # Pattern del nome file
    rotation="500 MB",                      # Ruota il file quando raggiunge 500MB
    retention="10 days",                    # Mantiene i log per 10 giorni
    level="INFO"                           # Livello di logging
)

def log_interaction(action: str, input_text: str, output_text: str, instruction: str = None):
    """
    Registra un'interazione con l'AI nel file di log.
    
    Questa funzione salva ogni interazione con l'AI in un file JSON separato,
    includendo timestamp, tipo di azione, input, output e istruzioni (se presenti).
    
    Args:
        action (str): Il tipo di azione eseguita (es. "organize", "edit")
        input_text (str): Il testo di input
        output_text (str): Il testo di output generato
        instruction (str, optional): L'istruzione fornita per la modifica
        
    Note:
        I file di log vengono salvati nella cartella prompts_logs/
        Ogni interazione genera un nuovo file JSON con timestamp
    """
    # Creazione dell'entry di log con tutte le informazioni rilevanti
    log_entry = {
        "timestamp": datetime.now().isoformat(),  # Timestamp ISO 8601
        "action": action,                         # Tipo di azione
        "input": input_text,                      # Testo di input
        "output": output_text,                    # Testo di output
        "instruction": instruction                # Istruzione (se presente)
    }
    
    # Creazione della directory dei log se non esiste
    os.makedirs("prompts_logs", exist_ok=True)
    
    # Generazione del nome file con timestamp
    log_file = f"prompts_logs/interaction_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    
    # Salvataggio del log in formato JSON
    with open(log_file, "w", encoding="utf-8") as f:
        json.dump(log_entry, f, ensure_ascii=False, indent=2)
    
    # Log aggiuntivo con loguru per tracciamento in tempo reale
    logger.info(f"Interaction logged: {action}") 