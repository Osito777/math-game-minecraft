import streamlit as st
import random

# --- CONFIGURACIÓN DE LA PÁGINA ---
st.set_page_config(page_title="Minecraft Math Boss Rush", page_icon="⚔️")

# --- ESTILO VISUAL MINECRAFT ---
st.markdown("""
    <style>
    .main { background-color: #0d0d0d; color: #ffffff; }
    .stButton>button { 
        width: 100%; 
        background-color: #2e2e2e; 
        color: #55FF55; 
        border: 2px solid #55FF55; 
        font-family: 'Courier New', monospace;
        font-size: 18px; 
    }
    .stButton>button:hover { background-color: #3e8e41; border-color: #ffffff; }
    h1 { color: #FF55FF; text-shadow: 2px 2px #000; font-family: 'Courier New'; text-align: center; }
    .boss-msg { color: #FF5555; font-size: 30px; font-weight: bold; text-align: center; text-shadow: 2px 2px #000; font-family: 'Courier New'; }
    .stRadio label { color: #FFFF55 !important; font-size: 20px !important; }
    </style>
    """, unsafe_allow_html=True)

# --- BASE DE DATOS DE PREGUNTAS (DIFICULTAD AUMENTADA) ---
if 'preguntas' not in st.session_state:
    # NIVEL 1: FÁCIL (Steve) - 6 Preguntas
    facil = [
        {"p": "Steve tiene $2^4$ bloques. Si explotan $\sqrt{16}$, ¿cuántos quedan?", "ops": ["12", "8", "4"], "c": "12"},
        {"p": "¿Cuál es la $\sqrt{144}$ multiplicada por $2$?", "ops": ["24", "12", "48"], "c": "24"},
        {"p": "Calcula: $3^3 + \sqrt{81}$", "ops": ["36", "30", "27"], "c": "36"},
        {"p": "Un cofre tiene $2^6$ espacios. Si usas la mitad, ¿cuántos quedan?", "ops": ["32", "16", "64"], "c": "32"},
        {"p": "Raíz cúbica de $64$ más $5^2$:", "ops": ["29", "21", "24"], "c": "29"},
        {"p": "FINAL NIVEL 1: $\sqrt{400} / 5$", "ops": ["4", "8", "20"], "c": "4"}
    ]
    # NIVEL 2
