import os
from openai import AsyncOpenAI
from app.prompts.editor_prompt import EDITOR_PROMPT

client = AsyncOpenAI(api_key=os.getenv("OPENAI_API_KEY"))

async def edit_text(text: str, instruction: str) -> str:
    """
    Modifica il testo secondo le istruzioni fornite (es. tono, stile, chiarezza).
    """
    try:
        response = await client.chat.completions.create(
            model="gpt-4",
            messages=[
                {"role": "system", "content": EDITOR_PROMPT},
                {"role": "user", "content": f"Testo da modificare:\n{text}\n\nIstruzione: {instruction}"}
            ],
            temperature=0.7,
            max_tokens=2000
        )
        
        edited_text = response.choices[0].message.content
        return edited_text
    except Exception as e:
        raise Exception(f"Errore durante la modifica del testo: {str(e)}") 