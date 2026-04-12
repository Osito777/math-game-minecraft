import streamlit as st

st.set_page_config(page_title="Math Craft", page_icon="⚔️")

# Estilo
st.markdown("<style>.main{background-color:#0d0d0d;color:white}button{width:100%}</style>", unsafe_allow_html=True)

if 'preguntas' not in st.session_state:
    f = [
        {"p": "Steve tiene 2^4 bloques. Si explotan raiz de 16, quedan?", "ops": ["12", "8", "4"], "c": "12"},
        {"p": "Raiz de 144 multiplicado por 2", "ops": ["24", "12", "48"], "c": "24"},
        {"p": "3^3 + Raiz de 81", "ops": ["36", "30", "27"], "c": "36"},
        {"p": "2^6 espacios. Mitad ocupada, quedan?", "ops": ["32", "16", "64"], "c": "32"},
        {"p": "Raiz cubica de 64 + 5^2", "ops": ["29", "21", "24"], "c": "29"},
        {"p": "Nivel 1: Raiz de 400 dividido 5", "ops": ["4", "8", "20"], "c": "4"}
    ]
    m = [
        {"p": "WITHER: (2^3)^2 - Raiz de 16", "ops": ["60", "32", "64"], "c": "60"},
        {"p": "Raiz de la raiz de 625", "ops": ["5", "25", "10"], "c": "5"},
        {"p": "Que es mayor: 5^3 o 11^2?", "ops": ["5^3", "11^2", "Iguales"], "c": "5^3"},
        {"p": "Raiz de 225 x Raiz de 4", "ops": ["30", "15", "60"], "c": "30"},
        {"p": "Portal: alto R-144, ancho R-100. Area?", "ops": ["120", "22", "200"], "c": "120"},
        {"p": "4^3 - 3^4", "ops": ["-17", "17", "7"], "c": "-17"},
        {"p": "Nivel 2: R-cubica 1000 x 2^3", "ops": ["80", "60", "100"], "c": "80"}
    ]
    d = [
        {"p": "HARDCORE: R-16 x (3^4 / 9)", "ops": ["36", "27", "81"], "c": "36"},
        {"p": "(2^2 x 5^2) - Raiz de 144", "ops": ["88", "100", "76"], "c": "88"},
        {"p": "R-169 + R-196 + R-225", "ops": ["42", "30", "45"], "c": "42"},
        {"p": "2^7 / Raiz de 64", "ops": ["16", "32", "8"], "c": "16"},
        {"p": "Warden: R-cubica 216 + 7^2", "ops": ["55", "49", "60"], "c": "55"},
        {"p": "(10^2 - 8^2) + Raiz de 1", "ops": ["37", "36", "19"], "c": "37"},
        {"p": "FINAL: Raiz de
