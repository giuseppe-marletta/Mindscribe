# MindScribe - Il Tuo Co-Autore Intelligente

MindScribe è un'applicazione Python che utilizza l'intelligenza artificiale di Mistral per aiutarti a organizzare e modificare i tuoi testi in modo intelligente. L'applicazione è stata sviluppata come progetto per l'esame di "Agenti Intelligenti e Machine Learning".

## 🚀 Funzionalità

- **Organizzazione Automatica**: Trasforma testo non strutturato in documenti ben organizzati con capitoli e sezioni
- **Modifica Intelligente**: Modifica il tono e lo stile del testo secondo le tue preferenze
- **Esportazione**: Salva i documenti in formato Markdown
- **Logging**: Traccia tutte le interazioni con l'AI per la valutazione
- **Interfaccia Web**: UI intuitiva e user-friendly basata su Streamlit

## 📋 Prerequisiti

- Python 3.11+
- Mistral AI API Key (ottienila gratuitamente su [Mistral AI](https://console.mistral.ai/))


## 🛠️ Installazione

1. Clona il repository:
```bash
git clone https://github.com/giuseppe-marletta/Mindscribe.git
cd Mindscribe
```

2. Crea un ambiente virtuale e attivalo:
```bash
python3 -m venv venv
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

### Backend API

1. Avvia il server FastAPI:
```bash
uvicorn app.main:app --reload
```

2. L'API sarà disponibile su `http://localhost:8000`
3. Documentazione API disponibile su `http://localhost:8000/docs`

### Frontend Streamlit

1. In un nuovo terminale, avvia l'interfaccia Streamlit:
```bash
streamlit run app/frontend.py
```

2. Apri il browser all'indirizzo mostrato (solitamente `http://localhost:8501`)

### Utilizzo dell'Interfaccia

1. **Inserimento del Testo**:
   - Incolla o scrivi il tuo testo nell'area di input
   - Il testo può essere di qualsiasi lunghezza

2. **Organizzazione**:
   - Clicca su "Organizza il testo" per strutturare automaticamente il contenuto
   - Il testo verrà organizzato in capitoli e sezioni

3. **Modifica**:
   - Clicca su "Modifica il testo"
   - Inserisci l'istruzione di modifica (es. "rendi più formale")
   - Il testo verrà modificato secondo le tue indicazioni

4. **Esportazione**:
   - Usa il pulsante di esportazione per salvare il testo in Markdown
   - I file verranno salvati nella cartella `output/`

## 📁 Struttura del Progetto

```
mindscribe/
├── app/
│   ├── main.py          # Backend FastAPI
│   ├── frontend.py      # Interfaccia Streamlit
│   ├── routes.py        # Endpoint API
│   ├── agents/
│   │   ├── organizer.py # Agente organizzatore
│   │   ├── editor.py    # Agente editor
│   │   ├── prompts/
│   │   │   ├── organizer_prompt.txt
│   │   │   ├── editor_prompt.txt
│   │   ├── utils/
│   │   │   ├── io.py       # Gestione file
│   │   │   ├── logger.py   # Sistema di logging
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

