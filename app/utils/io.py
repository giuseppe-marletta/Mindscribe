import os
import markdown2
import pdfkit
from datetime import datetime

async def save_to_file(content: str, format: str) -> str:
    """
    Salva il contenuto in un file nel formato specificato (markdown o pdf).
    """
    # Crea la directory per i file di output se non esiste
    os.makedirs("output", exist_ok=True)
    
    timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
    
    if format.lower() == "markdown":
        file_path = f"output/document_{timestamp}.md"
        with open(file_path, "w", encoding="utf-8") as f:
            f.write(content)
        return file_path
        
    elif format.lower() == "pdf":
        # Prima converti in HTML
        html = markdown2.markdown(content)
        file_path = f"output/document_{timestamp}.pdf"
        
        # Converti HTML in PDF
        pdfkit.from_string(html, file_path)
        return file_path
        
    else:
        raise ValueError(f"Formato non supportato: {format}") 