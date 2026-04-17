import streamlit as st
import random

st.set_page_config(page_title="Math Craft: Ultra-Hardcore", page_icon="💀")

# --- ESTILO ---
st.markdown("""
    <style>
    .main { background-color: #0d0d0d; color: white; }
    .stButton>button { width: 100%; background-color: #1a1a1a; color: #FF5555; border: 2px solid #AA0000; font-family: monospace; }
    h1 { color: #AA00AA; text-shadow: 3px 3px #000; text-align: center; }
    .heart { color: #FF5555; font-size: 35px; text-align: center; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- INICIALIZACIÓN ---
if 'preguntas' not in st.session_state:
    # NIVEL 1: Raíces y potencias simples anidadas
    f = [
        {"p": "Calcula: raiz(raiz(81)) + 2^2", "ops": ["7", "13", "5"], "c": "7"},
        {"p": "Resuelve: (2^2)^2 + raiz(144)", "ops": ["28", "20", "32"], "c": "28"},
        {"p": "Steve encuentra raiz(raiz(16)) bloques. ¿Cuantos son?", "ops": ["2", "4", "8"], "c": "2"},
        {"p": "Calcula: raiz(4^2 + 3^2) * 2", "ops": ["10", "14", "26"], "c": "10"},
        {"p": "Resuelve: raiz(64) + (3^2)^1", "ops": ["17", "15", "73"], "c": "17"},
        {"p": "BOSS 1: raiz(raiz(256)) * 2^2", "ops": ["16", "8", "32"], "c": "16"}
    ]
    # NIVEL 2: El Wither acecha (Dificultad Media-Alta)
    m = [
        {"p": "WITHER: raiz(raiz(625)) + (2^2)^3", "ops": ["69", "21", "61"], "c": "69"},
        {"p": "Calcula: raiz(2^6 + 6^2) / 2", "ops": ["5", "10", "25"], "c": "5"},
        {"p": "Resuelve: (3^2)^2 - raiz(raiz(81))", "ops": ["78", "79", "80"], "c": "78"},
        {"p": "Portal: alto raiz(raiz(1296)), ancho raiz(49). ¿Area?", "ops": ["42", "36", "49"], "c": "42"},
        {"p": "Calcula: raiz(10^2 - (2^3)^2)", "ops": ["6", "8", "4"], "c": "6"},
        {"p": "Resuelve: raiz(raiz(raiz(65536)))", "ops": ["4", "2", "8"], "c": "4"},
        {"p": "BOSS 2: (2^3)^2 / raiz(raiz(256))", "ops": ["16", "32", "8"], "c": "16"}
    ]
    # NIVEL 3: El Warden (Hardcore Total)
    d = [
        {"p": "WARDEN: raiz((5^2)^2) - (2^2)^2", "ops": ["9", "1", "25"], "c": "9"},
        {"p": "Calcula: raiz(raiz(10000)) + (2^3)^2", "ops": ["74", "68", "72"], "c": "74"},
        {"p": "Resuelve: raiz(raiz(16)^2 + 3^2)", "ops": ["5", "7", "25"], "c": "5"},
        {"p": "Ghast: (2^2)^3 / raiz(raiz(16))", "ops": ["32", "16", "64"], "c": "32"},
        {"p": "Calcula: raiz(raiz(625)) * raiz(raiz(81))", "ops": ["15", "25", "9"], "c": "15"},
        {"p": "Resuelve: (2^2)^3 - raiz(raiz(1296))", "ops": ["58", "60", "62"], "c": "58"},
        {"p": "FINAL: raiz(raiz(raiz(256))^4) - 16", "ops": ["0", "2", "4"], "c": "0"}
    ]
    
    random.shuffle(f); random.shuffle(m); random.shuffle(d)
    st.session_state.preguntas = f + m + d
    
    for p in st.session_state.preguntas:
        random.shuffle(p["ops"])
        
    st.session_state.score = 0
    st.session_state.current = 0
    st.session_state.boss_active = False
    st.session_state.vidas = 5 

# --- LÓGICA DE DERROTA ---
if st.session_state.vidas <= 0:
    st.markdown("<h1>💀 GAME OVER 💀</h1>", unsafe_allow_html=True)
    st.image("https://media.tenor.com/7Yf0L2G1H6sAAAAi/minecraft-death.gif", width=700)
    st.error(f"Fuiste derrotado en el nivel {st.session_state.current + 1}. Tus matemáticas no fueron suficientes.")
    if st.button("VOLVER A INTENTAR (RESPAWN) 🔄"):
        del st.session_state.preguntas
        st.rerun()
    st.stop()

# --- INTERFAZ ---
curr = st.session_state.current
st.markdown(f"<p class='heart'>{'❤️' * st.session_state.vidas}</p>", unsafe_allow_html=True)

# --- BOSSES ---
if st.session_state.get('boss_active', False):
    bosses = {
        6: ["⚠️ EL ENDER DRAGON ACECHA", "https://media.tenor.com/I8CBI7yIlFsAAAAi/ender-dragon.gif", "ORO"],
        13: ["💀 EL WITHER HA DESPERTADO", "https://media1.tenor.com/m/0C4A0FJB1EQAAAAd/wither-dance.gif", "DIAMANTE"],
        20: ["🕶️ EL WARDEN TE ESCUCHA", "https://media.tenor.com/AAAQv0Hbb5wAAAAi/warden-minecraft-ward.gif", "NETHERITE"]
    }
    nombre, img, mat = bosses[curr]
    st.write(f"## {nombre}")
    st.image(img, width=700)
    if st.button(f"GOLPE MAESTRO CON {mat} ⚔️"):
        st.session_state.boss_active = False
        st.rerun()

# --- PREGUNTAS ---
elif curr < len(st.session_state.preguntas):
    q = st.session_state.preguntas[curr]
    if curr < 6: color, espada = "ORO", "https://media.tenor.com/S7_bQqzBXa8AAAAi/terraria.gif"
    elif curr < 13: color, espada = "DIAMANTE", "https://media.tenor.com/AzZN3_XFVCkAAAAi/minecraft-sword.gif"
    else: color, espada = "NETHERITE", "https://media.tenor.com/cf_fWrmI0ywAAAAi/nigerite-sword.gif"
    
    st.title("Math Craft: Ultra-Hardcore")
    c1, c2 = st.columns([3, 1])
    c1.write(f"**Desafío {curr + 1} / 20** | Score: {st.session_state.score}")
    c1.subheader(f"💀 {q['p']} 💀")
    c2.image(espada, width=80)
    
    res = st.radio("Respuesta:", q["ops"], key=f"r{curr}")
    if st.button(f"ATACAR CON {color} ⚔️"):
        if res == q["c"]:
            st.success("¡CRÍTICO!")
            st.session_state.score += 1
        else:
            st.error(f"¡FALLO! Perdiste un corazón. La respuesta era {q['c']}")
            st.session_state.vidas -= 1
        
        st.session_state.current += 1
        if st.session_state.current in [6, 13, 20]:
            st.session_state.boss_active = True
        st.rerun()
    st.progress(curr / 20)

else:
    st.balloons()
    st.title("🏆 ¡LEYENDA DEL INFINITO!")
    st.write(f"Sobreviviste con {st.session_state.vidas} corazones. ¡Eres un genio!")
    if st.button("REINICIAR MUNDO 🔄"):
        del st.session_state.preguntas
        st.rerun()
