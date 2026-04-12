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

# --- BASE DE DATOS DE PREGUNTAS ---
if 'preguntas' not in st.session_state:
    facil = [
        {"p": "Steve tiene $2^4$ bloques. Si explotan $\sqrt{16}$, ¿cuántos quedan?", "ops": ["12", "8", "4"], "c": "12"},
        {"p": "¿Cuál es la $\sqrt{144}$ multiplicada por $2$?", "ops": ["24", "12", "48"], "c": "24"},
        {"p": "Calcula: $3^3 + \sqrt{81}$", "ops": ["36", "30", "27"], "c": "36"},
        {"p": "Un cofre tiene $2^6$ espacios. Si usas la mitad, ¿cuántos quedan?", "ops": ["32", "16", "64"], "c": "32"},
        {"p": "Raíz cúbica de $64$ más $5^2$:", "ops": ["29", "21", "24"], "c": "29"},
        {"p": "FINAL NIVEL 1: $\sqrt{400} / 5$", "ops": ["4", "8", "20"], "c": "4"}
    ]
    medio = [
        {"p": "EL WITHER ACECHA: $(2^3)^2 - \sqrt{16}$", "ops": ["60", "32", "64"], "c": "60"},
        {"p": "Calcula la raíz de una raíz: $\sqrt{\sqrt{625}}$", "ops": ["5", "25", "10"], "c": "5"},
        {"p": "¿Qué es mayor: $5^3$ o $11^2$?", "ops": ["5^3", "11^2", "Iguales"], "c": "5^3"},
        {"p": "Resuelve: $\sqrt{225} \times \sqrt{4}$", "ops": ["30", "15", "60"], "c": "30"},
        {"p": "Si un portal mide $\sqrt{144}$ de alto y $\sqrt{100}$ de ancho, ¿cuál es su área?", "ops": ["120", "22", "200"], "c": "120"},
        {"p": "Calcula: $4^3 - 3^4$", "ops": ["-17", "17", "7"], "c": "-17"},
        {"p": "FINAL NIVEL 2: $\sqrt[3]{1000} \times 2^3$", "ops": ["80", "60", "100"], "c": "80"}
    ]
    dificil = [
        {"p": "HARDCORE: $\sqrt{16} \times (3^4 / 9)$", "ops": ["36", "27", "81"], "c": "36"},
        {"p": "Resuelve: $(2^2 \times 5^2) - \sqrt{144}$", "ops": ["88", "100", "76"], "c": "88"},
        {"p": "Calcula: $\sqrt{169} + \sqrt{196} + \sqrt{225}$", "ops": ["42", "30", "45"], "c": "42"},
        {"p": "Potencia extrema: $2^7 / \sqrt{64}$", "ops": ["16", "32", "8"], "c": "16"},
        {"p": "El Warden oye: $\sqrt[3]{216} + 7^2$", "ops": ["55", "49", "60"], "c": "55"},
        {"p": "Calcula: $(10^2 - 8^2) + \sqrt{1}$", "ops": ["37", "36", "19"], "c": "37"},
        {"p": "FINAL TOTAL: $\sqrt{625} - 5^2$", "ops": ["0", "5", "25"], "c": "0"}
    ]
    st.session_state.preguntas = facil + medio + dificil
    st.session_state.score = 0
    st.session_state.current = 0
    st.session_state.boss_active = False

# --- LÓGICA DE JEFES ---
if st.session_state.get('boss_active', False):
    curr = st.session_state.current
    if curr == 6:
        st.markdown("<p class='boss-msg'>⚠️ ¡EL ENDER DRAGON HA APARECIDO! ⚠️</p>", unsafe_allow_html=True)
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJtZzZ5NXF6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/H1SXXLaWirIEuC69Pk/giphy.gif")
        if st.button("USAR FLECHAS Y DERROTAR 🏹"):
            st.session_state.boss_active = False
            st.rerun()
    elif curr == 13:
        st.markdown("<p class='boss-msg'>💀 ¡EL WITHER ESTÁ AQUÍ! 💀</p>", unsafe_allow_html=True)
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmZyeXd4ZHJ6NXF6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/A6Prmit6dhv32/giphy.gif")
        if st.button("USAR ESPADA DE DIAMANTE ⚔️"):
            st.session_state.boss_active = False
            st.rerun()
    elif curr == 20:
        st.markdown("<p class='boss-msg'>🕶️ ¡EL WARDEN TE HA DETECTADO! 🕶️</p>", unsafe_allow_html=True)
        st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJtZzZ5NXF6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/X9YInZ3m9vM3A44L5C/giphy.gif")
        if st.button("LOGRAR EL ESCAPE FINAL 🏃"):
            st.session_state.boss_active = False
            st.rerun()

# --- LÓGICA DE PREGUNTAS ---
elif st.session_state.current < len(st.session_state.preguntas):
    curr = st.session_state.current
    q = st.session_state.preguntas[curr]
    
    tipo_nivel = "FÁCIL 🟢" if curr < 6 else "MEDIO 🟡" if curr < 13 else "HARDCORE 🔴"
    st.title(f"Minecraft Math: {tipo_nivel}")
    st.write(f"### Desafío {curr + 1} de 20")
    st.subheader(q["p"])
    
    ans = st.radio("Elige tu respuesta:", q["ops"], key=f"p_{curr}")
    
    if st.button("LANZAR ATAQUE ⚔️"):
        if ans == q["c"]:
            st.success("¡Impacto Crítico!")
            st.session_state.score += 1
        else:
            st.error(f"¡Fallaste! La respuesta era: {q['c']}")
        
        nuevo_indice = curr + 1
        st.session_state.current = nuevo_indice
        
        if nuevo_indice in [6, 13, 20]:
            st.session_state.boss_active = True
        
        st.rerun()
    st.progress(curr / 20)

# --- FINAL ---
else:
    st.balloons()
    st.title("🏆 ¡LEYENDA DE MINECRAFT!")
    st.write(f"Puntuación: **{st.session_state.score} / 20**")
    if st.button("REINICIAR MUNDO 🔄"):
        st.session_state.current = 0
        st.session_state.score = 0
        st.session_state.boss_active = False
        st.rerun()
