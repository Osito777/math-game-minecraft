import streamlit as st

# Configuración visual de Minecraft
st.set_page_config(page_title="Minecraft Math Quest", page_icon="⛏️")

# CSS para que parezca Minecraft
st.markdown("""
    <style>
    .main { background-color: #1e1e1e; color: #ffffff; }
    .stButton>button { 
        background-color: #555555; 
        color: #55FF55; 
        border: 2px solid #000;
        font-family: 'Courier New', monospace;
        width: 100%;
    }
    h1 { color: #55FF55; text-shadow: 2px 2px #000; font-family: 'Courier New'; }
    .stRadio label { color: #FFAA00 !important; font-weight: bold; }
    </style>
    """, unsafe_allow_html=True)

st.title("⛏️ MINECRAFT MATH: Potencia y Raíz")

# Base de datos de 20 preguntas
if 'preguntas' not in st.session_state:
    st.session_state.preguntas = [
        {"p": "Steve tiene $2^3$ bloques de oro. ¿Cuántos tiene?", "ops": ["6", "8", "16"], "c": "8"},
        {"p": "Un cuadrado de tierra tiene área de 49. ¿Cuánto mide su lado? ($\sqrt{49}$)", "ops": ["7", "9", "6"], "c": "7"},
        {"p": "Un Creeper tiene potencia $5^2$. ¿Cuánto es?", "ops": ["10", "25", "50"], "c": "25"},
        {"p": "La raíz cúbica de 27 antorchas es:", "ops": ["3", "9", "6"], "c": "3"},
        {"p": "Si crafteas $3^3$ flechas, ¿cuántas tienes?", "ops": ["9", "27", "81"], "c": "27"},
        {"p": "La $\sqrt{121}$ es el nivel de tu pico. ¿Qué nivel es?", "ops": ["11", "12", "10"], "c": "11"},
        {"p": "Un Ghast lanza $2^4$ bolas de fuego. ¿Cuántas son?", "ops": ["8", "16", "32"], "c": "16"},
        {"p": "La $\sqrt{144}$ es la altura de tu torre. ¿Cuánto mide?", "ops": ["12", "14", "10"], "c": "12"},
        {"p": "Tienes $10^2$ bloques de obsidiana. ¿Cuántos son?", "ops": ["100", "1000", "20"], "c": "100"},
        {"p": "Raíz cuadrada de 81 diamantes:", "ops": ["8", "9", "7"], "c": "9"},
        {"p": "Calcula $4^3$ para activar el portal:", "ops": ["16", "64", "32"], "c": "64"},
        {"p": "La $\sqrt[3]{64}$ bloques de madera es:", "ops": ["4", "8", "16"], "c": "4"},
        {"p": "Un enderman se teletransporta $6^2$ metros. ¿Cuánto es?", "ops": ["12", "36", "42"], "c": "36"},
        {"p": "La $\sqrt{169}$ es la distancia a la aldea:", "ops": ["13", "14", "15"], "c": "13"},
        {"p": "Si tienes $7^2$ panes, ¿cuántos tienes?", "ops": ["14", "49", "56"], "c": "49"},
        {"p": "La raíz cúbica de 1000 es:", "ops": ["10", "100", "30"], "c": "10"},
        {"p": "Un cofre doble tiene $2^6$ espacios. ¿Cuántos son?", "ops": ["12", "64", "32"], "c": "64"},
        {"p": "La $\sqrt{225}$ es tu puntuación:", "ops": ["15", "25", "5"], "c": "15"},
        {"p": "$3^4$ bloques de piedra rojiza:", "ops": ["12", "81", "27"], "c": "81"},
        {"p": "La $\sqrt{400}$ es la profundidad de la mina:", "ops": ["20", "40", "10"], "c": "20"}
    ]
    st.session_state.score = 0
    st.session_state.current = 0

# Lógica del juego
if st.session_state.current < len(st.session_state.preguntas):
    q = st.session_state.preguntas[st.session_state.current]
    st.write(f"### Reto {st.session_state.current + 1} de 20")
    st.subheader(q["p"])
    
    ans = st.radio("Selecciona tu respuesta:", q["ops"], key=f"r{st.session_state.current}")
    
    if st.button("¡ENVIAR RESPUESTA! ⚔️"):
        if ans == q["c"]:
            st.success("¡CORRECTO! Has ganado un diamante 💎")
            st.session_state.score += 1
        else:
            st.error(f"¡BOOM! Un TNT explotó. La respuesta era {q['c']} 🧨")
        
        st.session_state.current += 1
        st.button("Siguiente Pregunta 🏃")
else:
    st.balloons()
    st.write(f"## ¡Misión Cumplida, Minero! 🏆")
    st.write(f"Tu puntuación final es: **{st.session_state.score} / 20**")
    if st.button("Reiniciar Aventura"):
        st.session_state.current = 0
        st.session_state.score = 0
        st.rerun()
