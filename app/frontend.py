import streamlit as st
import requests
import json
from datetime import datetime
import os

# Configurazione della pagina
st.set_page_config(
    page_title="MindScribe - Il Tuo Co-Autore Intelligente",
    page_icon="📝",
    layout="wide"
)

# Stile CSS personalizzato
st.markdown("""
    <style>
    .main {
        padding: 2rem;
    }
    .stTextArea textarea {
        font-size: 16px;
    }
    .stButton button {
        width: 100%;
        margin-top: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

# Titolo e descrizione
st.title("📝 MindScribe")
st.markdown("""
    Benvenuto in MindScribe, il tuo assistente intelligente per la scrittura!
    Inserisci il tuo testo e lascia che l'AI lo organizzi e lo migliori per te.
""")

# Inizializzazione dello stato della sessione
if 'organized_text' not in st.session_state:
    st.session_state.organized_text = ""
if 'edited_text' not in st.session_state:
    st.session_state.edited_text = ""

# Funzione per chiamare l'API
def call_api(endpoint, data):
    try:
        response = requests.post(f"http://localhost:8000/{endpoint}", json=data)
        response.raise_for_status()
        return response.json()
    except Exception as e:
        st.error(f"Errore durante la chiamata all'API: {str(e)}")
        return None

# Input del testo
st.header("1️⃣ Inserisci il tuo testo")
text_input = st.text_area(
    "Scrivi o incolla qui il tuo testo",
    height=200,
    placeholder="Inserisci il testo che vuoi organizzare o modificare..."
)

# Pulsanti per le azioni principali
col1, col2 = st.columns(2)

with col1:
    if st.button("🔄 Organizza il testo", use_container_width=True):
        if text_input:
            with st.spinner("Organizzazione in corso..."):
                result = call_api("organize", {"content": text_input})
                if result:
                    st.session_state.organized_text = result["organized_text"]
                    st.success("Testo organizzato con successo!")
        else:
            st.warning("Per favore, inserisci del testo da organizzare.")

with col2:
    if st.button("✏️ Modifica il testo", use_container_width=True):
        if text_input:
            instruction = st.text_input("Come vuoi modificare il testo?", 
                                      placeholder="Es: rendi più formale, più conciso, più tecnico...")
            if instruction:
                with st.spinner("Modifica in corso..."):
                    result = call_api("edit", {
                        "content": text_input,
                        "instruction": instruction
                    })
                    if result:
                        st.session_state.edited_text = result["edited_text"]
                        st.success("Testo modificato con successo!")
        else:
            st.warning("Per favore, inserisci del testo da modificare.")

# Visualizzazione dei risultati
if st.session_state.organized_text:
    st.header("📚 Testo Organizzato")
    st.markdown(st.session_state.organized_text)
    
    # Opzioni di esportazione per il testo organizzato
    col3, col4 = st.columns(2)
    with col3:
        if st.button("📥 Scarica come Markdown", use_container_width=True):
            result = call_api("export", {
                "content": st.session_state.organized_text,
                "format": "markdown"
            })
            if result:
                st.success(f"File salvato in: {result['file_path']}")
    
    with col4:
        if st.button("📄 Scarica come PDF", use_container_width=True):
            result = call_api("export", {
                "content": st.session_state.organized_text,
                "format": "pdf"
            })
            if result:
                st.success(f"File salvato in: {result['file_path']}")

if st.session_state.edited_text:
    st.header("✏️ Testo Modificato")
    st.markdown(st.session_state.edited_text)
    
    # Opzioni di esportazione per il testo modificato
    col5, col6 = st.columns(2)
    with col5:
        if st.button("📥 Scarica come Markdown (Modificato)", use_container_width=True):
            result = call_api("export", {
                "content": st.session_state.edited_text,
                "format": "markdown"
            })
            if result:
                st.success(f"File salvato in: {result['file_path']}")
    
    with col6:
        if st.button("📄 Scarica come PDF (Modificato)", use_container_width=True):
            result = call_api("export", {
                "content": st.session_state.edited_text,
                "format": "pdf"
            })
            if result:
                st.success(f"File salvato in: {result['file_path']}")

# Footer
st.markdown("---")
st.markdown("""
    <div style='text-align: center'>
        <p>MindScribe - Il Tuo Co-Autore Intelligente</p>
        <p>Creato con ❤️ per l'esame di Agenti Intelligenti e Machine Learning</p>
    </div>
""", unsafe_allow_html=True) 