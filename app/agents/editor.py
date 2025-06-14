# Importazione delle librerie necessarie
import os
from mistralai.client import MistralClient
from mistralai.models.chat_completion import ChatMessage
from app.prompts.editor_prompt import EDITOR_PROMPT

# Inizializzazione del client Mistral
# Utilizza la chiave API dalle variabili d'ambiente
client = MistralClient(api_key=os.getenv("MISTRAL_API_KEY"))

async def edit_text(text: str, instruction: str) -> str:
    """
    Modifica il testo secondo le istruzioni fornite (es. tono, stile, chiarezza).
    
    Questa funzione utilizza Mistral AI per modificare il testo mantenendo il significato
    originale ma adattando lo stile e il tono secondo le istruzioni specificate.
    
    Args:
        text (str): Il testo da modificare
        instruction (str): L'istruzione per la modifica (es. "rendi più formale")
        
    Returns:
        str: Il testo modificato
        
    Raises:
        Exception: Se si verifica un errore durante l'elaborazione con Mistral AI
    """
    try:
        # Preparazione dei messaggi per la chat
        messages = [
            ChatMessage(role="system", content=EDITOR_PROMPT),
            ChatMessage(role="user", content=f"Testo da modificare:\n{text}\n\nIstruzione: {instruction}")
        ]
        
        # Chiamata all'API di Mistral
        response = client.chat(
            model="mistral-large-latest",  # Utilizzo del modello più recente di Mistral
            messages=messages,
            temperature=0.7,  # Bilancia tra creatività e coerenza
            max_tokens=2000   # Limite di token per la risposta
        )
        
        # Estrazione del testo modificato dalla risposta
        edited_text = response.choices[0].message.content
        return edited_text
    except Exception as e:
        # Gestione degli errori con messaggio descrittivo
        raise Exception(f"Errore durante la modifica del testo: {str(e)}") 