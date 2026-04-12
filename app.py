import streamlit as st
import random

# Configuración visual de Minecraft
st.set_page_config(page_title="Minecraft Hardcore Math", page_icon="💀")

# CSS para estilo Minecraft Avanzado
st.markdown("""
    <style>
    .main { background-color: #0f0f0f; color: #ffffff; }
    .stButton>button { 
        background-color: #3c3c3c; 
        color: #55FF55; 
        border: 2px solid #000;
        font-family: 'Courier New', monospace;
        font-size: 20px;
    }
    h1 { color: #AA0000; text-shadow: 3px 3px #000; font-family: 'Courier New'; }
    .stRadio label { color: #00AAAA !important; font-size: 18px; }
    </style>
    """, unsafe_allow_html=True)

st.title("💀 MINECRAFT MATH: Nivel Hardcore")

# Banco de 20 preguntas COMPLEJAS
if 'preguntas' not in st.session_state:
    db = [
        {"p": "Calcula la potencia de un faro: $(2^2)^3$. ¿Cuántos bloques de alcance tiene?", "ops": ["12", "64", "32"], "c": "64"},
        {"p": "Un mapa del tesoro indica una distancia de $\sqrt{\sqrt{256}}$ chunks. ¿Cuánto es?", "ops": ["16", "4", "8"], "c": "4"},
        {"p": "Para invocar al Wither necesitas $3^4 - 2^5$ bloques. ¿Cuántos son?", "ops": ["49", "17", "43"], "c": "49"},
        {"p": "La raíz cuadrada de la potencia $10^4$ es:", "ops": ["100", "1000", "50"], "c": "100"},
        {"p": "Calcula el volumen de un cubo de TNT si su lado es $\sqrt{64}$:", "ops": ["512", "64", "256"], "c": "512"},
        {"p": "¿Cuál es el valor de $5^3 + \sqrt{144}$?", "ops": ["137", "113", "144"], "c": "137"},
        {"p": "Un Enderman se mueve a $(3^2)^2$ metros de distancia. ¿Cuánto es?", "ops": ["18", "81", "27"], "c": "81"},
        {"p": "La raíz cúbica de $8^2$ es equivalente a:", "ops": ["4", "2", "8"], "c": "4"},
        {"p": "Si un stack de diamantes se eleva a la potencia 0 ($64^0$), ¿cuántos tienes?", "ops": ["0", "1", "64"], "c": "1"},
        {"p": "Calcula: $\sqrt{100} + \sqrt{81} + \sqrt{64}$", "ops": ["27", "24", "25"], "c": "27"},
        {"p": "Un servidor tiene $2^{10}$ espacios para jugadores. ¿Cuántos son?", "ops": ["512", "1024", "2048"], "c": "1024"},
        {"p": "La mitad de la raíz cuadrada de 400 es:", "ops": ["20", "10", "5"], "c": "10"},
        {"p": "¿Qué es mayor: $2^6$ o $4^3$?", "ops": ["Son iguales", "2^6 es mayor", "4^3 es mayor"], "c": "Son iguales"},
        {"p": "Calcula: $(10^2 - 8^2)$ y saca su raíz cuadrada:", "ops": ["6", "4", "2"], "c": "6"},
        {"p": "La potencia $7^3$ representa los bloques de una pirámide. ¿Cuánto es?", "ops": ["243", "343", "49"], "c": "343"},
        {"p": "Si $\sqrt{x} = 14$, ¿cuántos bloques vale x?", "ops": ["196", "169", "256"], "c": "196"},
        {"p": "Calcula la raíz cúbica de $216$:", "ops": ["4", "6", "8"], "c": "6"},
        {"p": "Resuelve: $2^3 \times \sqrt{16}$", "ops": ["32", "24", "48"], "c": "32"},
        {"p": "El área de una base es $12^2$. Si le quitas $\sqrt{100}$, ¿cuánto queda?", "ops": ["134", "44", "24"], "c": "134"},
        {"p": "¿Cuál es la raíz cuadrada de $2^8$?", "ops": ["16", "32", "64"], "c": "16"}
    ]
    random.shuffle(db) # Esto desordena las preguntas cada vez
    st.session_state.preguntas = db
    st.session_state.score = 0
    st.session_state.current = 0

# Lógica del juego
if st.session_state.current < len(st.session_state.preguntas):
    q = st.session_state.preguntas[st.session_state.current]
    st.write(f"### NIVEL {st.session_state.current + 1} / 20")
    st.subheader(q["p"])
    
    ans = st.radio("Selecciona tu respuesta:", q["ops"], key=f"r{st.session_state.current}")
    
    col1, col2 = st.columns(2)
    with col1:
        if st.button("ATACAR ⚔️"):
            if ans == q["c"]:
                st.success("¡CRÍTICO! Has derrotado al mob 💎")
                st.session_state.score += 1
            else:
                st.error(f"¡PERDISTE VIDA! La respuesta era {q['c']} 💔")
            
            st.session_state.current += 1
            st.rerun()

    st.progress(st.session_state.current / 20)
else:
    st.balloons()
    st.write(f"## 🏆 ¡HAS SOBREVIVIDO AL MODO HARDCORE!")
    st.write(f"Puntuación final: **{st.session_state.score} / 20**")
    if st.button("Reiniciar Mundo"):
        del st.session_state.preguntas
        st.rerun()
