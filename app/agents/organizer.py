# Importazione delle librerie necessarie
import os
from mistralai.client import MistralClient
from app.prompts.organizer_prompt import ORGANIZER_PROMPT

# Inizializzazione del client Mistral
# Utilizza la chiave API dalle variabili d'ambiente
client = MistralClient(api_key=os.getenv("MISTRAL_API_KEY"))

async def organize_text(text: str) -> str:
    """
    Organizza il testo in input in una struttura logica di capitoli e sezioni.
    
    Questa funzione utilizza Mistral AI per analizzare il testo e riorganizzarlo in una
    struttura gerarchica con capitoli, sezioni e paragrafi ben definiti.
    
    Args:
        text (str): Il testo da organizzare
        
    Returns:
        str: Il testo organizzato in formato Markdown
        
    Raises:
        Exception: Se si verifica un errore durante l'elaborazione con Mistral AI
    """
    try:
        # Preparazione dei messaggi per la chat
        messages = [
            {"role": "system", "content": ORGANIZER_PROMPT},
            {"role": "user", "content": text}
        ]
        
        # Chiamata all'API di Mistral
        response = client.chat(
            model="mistral-large-latest",  # Utilizzo del modello più recente di Mistral
            messages=messages,
            temperature=0.7,  # Bilancia tra creatività e coerenza
            max_tokens=8000   # Limite di token per la risposta
        )
        
        # Estrazione del testo organizzato dalla risposta
        organized_text = response.choices[0].message.content
        return organized_text
    except Exception as e:
        # Gestione degli errori con messaggio descrittivo
        raise Exception(f"Errore durante l'organizzazione del testo: {str(e)}") 