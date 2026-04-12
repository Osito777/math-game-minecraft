import streamlit as st
import random

st.set_page_config(page_title="Minecraft Math", page_icon="⚔️")

st.markdown("""
    <style>
    .main { background-color: #0d0d0d; color: #ffffff; }
    .stButton>button { width: 100%; background-color: #2e2e2e; color: #55FF55; border: 2px solid #55FF55; font-family: monospace; }
    h1 { color: #FF55FF; text-shadow: 2px 2px #000; text-align: center; }
    .boss-msg { color: #FF5555; font-size: 30px; font-weight: bold; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

if 'preguntas' not in st.session_state:
    f = [
        {"p": "Steve tiene 2^4 bloques. Si explotan la raiz de 16, ¿cuantos quedan?", "ops": ["12", "8", "4"], "c": "12"},
        {"p": "Calcula: Raiz de 144 multiplicado por 2", "ops": ["24", "12", "48"], "c": "24"},
        {"p": "Resuelve: 3^3 + Raiz de 81", "ops": ["36", "30", "27"], "c": "36"},
        {"p": "2^6 espacios en un cofre. Mitad ocupada, ¿cuantos quedan?", "ops": ["32", "16", "64"], "c": "32"},
        {"p": "Raiz cubica de 64 + 5^2", "ops": ["29", "21", "24"], "c": "29"},
        {"p": "FINAL NIVEL 1: Raiz de 400 dividido 5", "ops": ["4", "8", "20"], "c": "4"}
    ]
    m = [
        {"p": "WITHER: (2^3)^2 - Raiz de 16", "ops": ["60", "32", "64"], "c": "60"},
        {"p": "Calcula la raiz de la raiz de 625", "ops": ["5", "25", "10"], "c": "5"},
        {"p": "¿Que
