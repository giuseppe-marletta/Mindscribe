import os
import json
from datetime import datetime
from loguru import logger

# Configura il logger
logger.add(
    "prompts_logs/mindscribe_{time}.log",
    rotation="500 MB",
    retention="10 days",
    level="INFO"
)

def log_interaction(action: str, input_text: str, output_text: str, instruction: str = None):
    """
    Registra un'interazione con l'AI nel file di log.
    """
    log_entry = {
        "timestamp": datetime.now().isoformat(),
        "action": action,
        "input": input_text,
        "output": output_text,
        "instruction": instruction
    }
    
    # Assicurati che la directory esista
    os.makedirs("prompts_logs", exist_ok=True)
    
    # Salva il log in formato JSON
    log_file = f"prompts_logs/interaction_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"
    with open(log_file, "w", encoding="utf-8") as f:
        json.dump(log_entry, f, ensure_ascii=False, indent=2)
    
    # Log anche con loguru
    logger.info(f"Interaction logged: {action}") 