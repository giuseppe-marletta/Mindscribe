# MindScribe - Il Tuo Co-Autore Intelligente

MindScribe è un'applicazione Python che utilizza l'intelligenza artificiale di Mistral per aiutarti a organizzare e modificare i tuoi testi in modo intelligente. L'applicazione è stata sviluppata come progetto per l'esame di "Agenti Intelligenti e Machine Learning".

## 🚀 Funzionalità

- **Organizzazione Automatica**: Trasforma testo non strutturato in documenti ben organizzati con capitoli e sezioni
- **Modifica Intelligente**: Modifica il tono e lo stile del testo secondo le tue preferenze
- **Esportazione**: Salva i documenti in formato Markdown o PDF
- **Logging**: Traccia tutte le interazioni con l'AI per la valutazione

## 📋 Prerequisiti

- Python 3.11+
- Mistral AI API Key
- wkhtmltopdf (per l'esportazione PDF)

## 🛠️ Installazione

1. Clona il repository:
```bash
git clone https://github.com/tuousername/mindscribe.git
cd mindscribe
```

2. Crea un ambiente virtuale e attivalo:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
# oppure
.\venv\Scripts\activate  # Windows
```

3. Installa le dipendenze:
```bash
pip install -r requirements.txt
```

4. Crea un file `.env` nella root del progetto e aggiungi la tua Mistral API Key:
```
MISTRAL_API_KEY=your_api_key_here
```

## 🚀 Utilizzo

1. Avvia il server:
```bash
uvicorn app.main:app --reload
```

2. L'API sarà disponibile su `http://localhost:8000`

3. Documentazione API disponibile su `http://localhost:8000/docs`

### Endpoint Principali

- `POST /organize`: Organizza il testo in input
- `POST /edit`: Modifica il testo secondo le istruzioni
- `POST /export`: Esporta il testo in Markdown o PDF

## 📝 Esempio di Utilizzo

```python
import requests

# Organizza un testo
response = requests.post("http://localhost:8000/organize", 
    json={"content": "Il tuo testo qui..."})
organized_text = response.json()["organized_text"]

# Modifica il testo
response = requests.post("http://localhost:8000/edit",
    json={
        "content": organized_text,
        "instruction": "Rendi il testo più formale"
    })
edited_text = response.json()["edited_text"]

# Esporta in PDF
response = requests.post("http://localhost:8000/export",
    json={
        "content": edited_text,
        "format": "pdf"
    })
```

## 📁 Struttura del Progetto

```
mindscribe/
├── app/
│   ├── main.py
│   ├── routes.py
│   ├── agents/
│   │   ├── organizer.py
│   │   ├── editor.py
│   ├── prompts/
│   │   ├── organizer_prompt.txt
│   │   ├── editor_prompt.txt
│   ├── utils/
│   │   ├── io.py
│   │   ├── logger.py
├── requirements.txt
├── .env
└── README.md
```

## 📊 Log delle Interazioni

Tutte le interazioni con l'AI vengono registrate nella cartella `prompts_logs/` in formato JSON. Questi log sono essenziali per la valutazione del progetto.

## 🤝 Contribuire

Le pull request sono benvenute. Per modifiche importanti, apri prima un issue per discutere cosa vorresti cambiare.

## 📄 Licenza

[MIT](https://choosealicense.com/licenses/mit/)
