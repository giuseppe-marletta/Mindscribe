import os
from openai import AsyncOpenAI
from app.prompts.organizer_prompt import ORGANIZER_PROMPT

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def organize_text(text: str) -> str:
    """
    Organizza il testo in input in una struttura logica di capitoli e sezioni.
    """
    try:
        response = await client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": ORGANIZER_PROMPT},
                {"role": "user", "content": text}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        
        organized_text = response.choices[0].message.content
        return organized_text
    except Exception as e:
        raise Exception(f"Errore durante l'organizzazione del testo: {str(e)}") 