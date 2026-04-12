import streamlit as st
import random
import time

# Configuración visual
st.set_page_config(page_title="Minecraft Boss Rush", page_icon="⚔️")

# Estilo Minecraft
st.markdown("""
    <style>
    .main { background-color: #121212; color: #ffffff; }
    .stButton>button { width: 100%; background-color: #3e3e3e; color: #55FF55; border: 2px solid #000; }
    h1 { color: #FF55FF; text-shadow: 2px 2px #000; font-family: 'Courier New'; }
    .boss-msg { color: #FF5555; font-size: 25px; font-weight: bold; text-align: center; }
    </style>
    """, unsafe_allow_html=True)

# 1. Base de datos de preguntas por niveles
if 'preguntas' not in st.session_state:
    facil = [
        {"p": "Steve tiene $2^3$ bloques de oro. ¿Cuántos son?", "ops": ["6", "8", "16"], "c": "8"},
        {"p": "Raíz cuadrada de 49: $\sqrt{49}$", "ops": ["7", "9", "6"], "c": "7"},
        {"p": "Un stack es $4^3$. ¿Cuántos bloques tiene?", "ops": ["16", "64", "32"], "c": "64"},
        {"p": "La $\sqrt{64}$ espacios de un cofre:", "ops": ["8", "6", "10"], "c": "8"},
        {"p": "Calcula $5^2$ antorchas:", "ops": ["10", "25", "50"], "c": "25"},
        {"p": "Raíz cúbica de 27: $\sqrt[3]{27}$", "ops": ["3", "9", "6"], "c": "3"}
    ]
    medio = [
        {"p": "Calcula: $(3^2)^2$ metros de distancia:", "ops": ["18", "81", "27"], "c": "81"},
        {"p": "Raíz de raíz: $\sqrt{\sqrt{256}}$", "ops": ["4", "8", "16"], "c": "4"},
        {"p": "Resuelve: $2^5 - 10$", "ops": ["22", "32", "12"], "c": "22"},
        {"p": "La $\sqrt{144} + \sqrt{25}$ es:", "ops": ["17", "19", "13"], "c": "17"},
        {"p": "Potencia de $4^3$ dividido entre 2:", "ops": ["32", "16", "64"], "c": "32"},
        {"p": "Raíz cúbica de 125: $\sqrt[3]{125}$", "ops": ["5", "15", "25"], "c": "5"},
        {"p": "Si $x^2 = 121$, ¿cuánto vale x?", "ops": ["11", "12", "13"], "c": "11"}
    ]
    dificil = [
        {"p": "HARDCORE: $\sqrt{100} + 3^3 - \sqrt{81}$", "ops": ["28", "30", "26"], "c": "28"},
        {"p": "Calcula: $(10^2 - 8^2)$ y saca su raíz:", "ops": ["6", "4", "36"], "c": "6"},
        {"p": "Potencia de potencias: $(2^3)^2$", "ops": ["64", "32", "16"], "c": "64"},
        {"p": "La $\sqrt{225}$ multiplicada por 2:", "ops": ["30", "25", "45"], "c": "30"},
        {"p": "Raíz cúbica de $216$:", "ops": ["6", "8", "4"], "c": "6"},
        {"p": "Resuelve: $7^2 + \sqrt{1}$", "ops": ["50", "49", "51"], "c": "50"},
        {"p": "FINAL: $\sqrt{16} \times 2^2$", "ops": ["16", "8", "32"], "c": "16"}
    ]
    st.session_state.preguntas = facil + medio + dificil
    st.session_state.score = 0
    st.session_state.current = 0
    st.session_state.boss_visible = False

# Función para mostrar animaciones de Jefes
def mostrar_jefe(nombre, gif_url):
    st.markdown(f"<p class='boss-msg'>¡JEFE APARECE: {nombre}!</p>", unsafe_allow_html=True)
    st.image(gif_url)
    if st.button(f"DERROTAR AL {nombre} ⚔️"):
        st.session_state.boss_visible = False
        st.session_state.current += 1
        st.rerun()

# 2. Lógica de niveles y animaciones
curr = st.session_state.current

# Verificar si toca Boss
if curr == 6 and st.session_state.boss_visible: # Fin Nivel Fácil
    mostrar_jefe("ENDER DRAGON", "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJtZzZ5NXF6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/H1SXXLaWirIEuC69Pk/giphy.gif")
elif curr == 13 and st.session_state.boss_visible: # Fin Nivel Medio
    mostrar_jefe("WITHER", "https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExbmZyeXd4ZHJ6NXF6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/A6Prmit6dhv32/giphy.gif")
elif curr == 20: # Fin del Juego
    st.balloons()
    st.image("https://media.giphy.com/media/v1.Y2lkPTc5MGI3NjExNHJtZzZ5NXF6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6ZzR6JmVwPXYxX2ludGVybmFsX2dpZl9ieV9pZCZjdD1n/X9YInZ3m9vM3A44L5C/giphy.gif") # Warden / Win
    st.write(f"## 🏆 ¡ERES EL REY DE LAS MATEMÁTICAS! Score: {st.session_state.score}/20")
    if st.button("Reiniciar"):
        st.session_state.current = 0
        st.session_state.score = 0
        st.rerun()
else:
    # Mostrar Preguntas
    q = st.session_state.preguntas[curr]
    st.title(f"Nivel: {'Fácil' if curr < 6 else 'Medio' if curr < 13 else 'DIFÍCIL'}")
    st.write(f"### Pregunta {curr + 1}")
    st.subheader(q["p"])
    
    ans = st.radio("Alternativas:", q["ops"], key=f"r{curr}")
    
    if st.button("ENVIAR ⚔️"):
        if ans == q["c"]:
            st.success("¡ACIERTO!")
            st.session_state.score += 1
        else:
            st.error(f"¡FALLO! Era {q['c']}")
        
        # Activar Boss si es la última del nivel
        if curr in [5, 12, 19]:
            st.session_state.boss_visible = True
        else:
            st.session_state.current += 1
        st.rerun()
