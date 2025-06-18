# Importazione delle librerie necessarie
import os
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
import json
from datetime import datetime
import logging

# Assicurati che la directory dei log esista
os.makedirs('prompts_logs', exist_ok=True)

# Configurazione del logging
logging.basicConfig(
    filename=f'prompts_logs/mindscribe_{datetime.now().strftime("%Y-%m-%d_%H-%M-%S")}_{os.getpid()}.log',
    level=logging.INFO,
    format='%(asctime)s - %(levelname)s - %(message)s'
)

# Inizializzazione del client Mistral
# Utilizza la chiave API dalle variabili d'ambiente
client = MistralClient(api_key=os.getenv("MISTRAL_API_KEY"))

def validate_modification_instruction(instruction: str) -> bool:
    """
    Valida l'istruzione di modifica per assicurarsi che sia sensata.
    Restituisce True se l'istruzione è valida, False altrimenti.
    """
    # Rimuovi spazi extra e converti in minuscolo
    instruction = instruction.strip().lower()
    
    # Lista di parole chiave che indicano un'istruzione valida
    valid_keywords = [
        'rendi', 'modifica', 'cambia', 'trasforma', 'adatta',
        'più', 'meno', 'migliora', 'semplifica', 'complica',
        'formale', 'informale', 'tecnico', 'semplice', 'complesso',
        'chiaro', 'conciso', 'dettagliato', 'breve', 'lungo',
        'aggiungi', 'rimuovi', 'espandi', 'riduci', 'riorganizza',
        'struttura', 'formatta', 'stile', 'tono', 'linguaggio'
    ]
    
    # Verifica se l'istruzione contiene almeno una parola chiave valida
    return any(keyword in instruction for keyword in valid_keywords)

async def edit_text(text: str, modification_instruction: str) -> str:
    """
    Modifica il testo secondo le istruzioni fornite.
    
    Questa funzione utilizza Mistral AI per modificare il testo mantenendo il significato
    originale ma adattando lo stile e il tono secondo le istruzioni specificate.
    
    Args:
        text (str): Il testo da modificare
        modification_instruction (str): L'istruzione per la modifica (es. "rendi più formale")
        
    Returns:
        str: Il testo modificato
        
    Raises:
        Exception: Se si verifica un errore durante l'elaborazione con Mistral AI
    """
    try:
        # Valida l'istruzione di modifica
        if not validate_modification_instruction(modification_instruction):
            return "Errore: L'istruzione di modifica non è valida. Per favore, fornisci un'istruzione chiara su come modificare il testo (es. 'rendi più formale', 'semplifica il linguaggio', ecc.)."
        
        # Carica il prompt di sistema
        with open('app/prompts/editor_prompt.txt', 'r', encoding='utf-8') as f:
            system_prompt = f.read()
        
        # Prepara il prompt utente
        user_prompt = f"""Testo da modificare:
{text}

Istruzione di modifica: {modification_instruction}

Per favore, modifica il testo secondo l'istruzione fornita. Mantieni la struttura e il significato originale, ma applica le modifiche richieste."""
        
        # Log della richiesta
        logging.info(f"Richiesta di modifica testo - Istruzione: {modification_instruction}")
        
        # Chiamata all'API
        chat_response = client.chat(
            model="mistral-large-latest",
            messages=[
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_prompt}
            ],
            max_tokens=8000,   # Limite di token per la risposta
            temperature=0.7
        )
        
        # Log della risposta
        logging.info(f"Risposta ricevuta: {chat_response.choices[0].message.content[:100]}...")
        
        return chat_response.choices[0].message.content
        
    except Exception as e:
        logging.error(f"Errore durante la modifica del testo: {str(e)}")
        return f"Si è verificato un errore durante la modifica del testo: {str(e)}" 