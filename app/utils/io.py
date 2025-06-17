# Importazione delle librerie necessarie
import os
import markdown2
import pdfkit
from datetime import datetime

async def save_to_file(content: str, format: str) -> str:
    """
    Salva il contenuto in un file nel formato specificato (markdown o pdf).
    
    Questa funzione gestisce il salvataggio del contenuto in diversi formati,
    supportando sia Markdown che PDF. Per il formato PDF, il contenuto viene
    prima convertito in HTML e poi in PDF.
    
    Args:
        content (str): Il contenuto da salvare
        format (str): Il formato di output ("markdown" o "pdf")
        
    Returns:
        str: Il percorso del file salvato
        
    Raises:
        ValueError: Se il formato specificato non è supportato
        Exception: Se si verifica un errore durante il salvataggio
        
    Note:
        Per l'esportazione in PDF è necessario avere wkhtmltopdf installato
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
        
    elif format.lower() == "pdf":
        try:
            # Conversione in PDF
            # Prima converti il Markdown in HTML
            html = markdown2.markdown(content)
            file_path = f"output/document_{timestamp}.pdf"
            
            # Converti l'HTML in PDF usando pdfkit
            try:
                pdfkit.from_string(html, file_path)
                return file_path
            except Exception as e:
                if "wkhtmltopdf" in str(e).lower():
                    raise Exception("Per esportare in PDF è necessario installare wkhtmltopdf. Per favore, installalo dal sito ufficiale: https://wkhtmltopdf.org/downloads.html")
                else:
                    raise Exception(f"Errore durante la conversione in PDF: {str(e)}")
        except Exception as e:
            raise Exception(f"Errore durante la generazione del PDF: {str(e)}")
        
    else:
        # Gestione del formato non supportato
        raise ValueError(f"Formato non supportato: {format}") 