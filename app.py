import streamlit as st
import random

st.set_page_config(page_title="Math Craft: Hardcore", page_icon="💀")

# --- ESTILO ---
st.markdown("""
    <style>
    .main { background-color: #0d0d0d; color: white; }
    .stButton>button { width: 100%; background-color: #2e2e2e; color: #FF5555; border: 2px solid #FF5555; font-family: monospace; }
    h1 { color: #FF55FF; text-shadow: 2px 2px #000; text-align: center; }
    .heart { color: #FF5555; font-size: 30px; text-align: center; margin-bottom: 20px; }
    </style>
    """, unsafe_allow_html=True)

# --- INICIALIZACIÓN ---
if 'preguntas' not in st.session_state:
    # Preguntas de alta dificultad
    f = [
        {"p": "Steve tiene 2^5 bloques. Explota la raiz de 64. ¿Quedan?", "ops": ["24", "26", "28"], "c": "24"},
        {"p": "Raiz de 256 dividido por 2^2", "ops": ["4", "8", "16"], "c": "4"},
        {"p": "Un Creeper hace 3^2 + 4^2 de daño. ¿Total?", "ops": ["25", "49", "14"], "c": "25"},
        {"p": "2^4 + 3^3 - raiz de 49", "ops": ["36", "40", "33"], "c": "36"},
        {"p": "Raiz cubica de 125 multiplicada por 2^3", "ops": ["40", "15", "60"], "c": "40"},
        {"p": "BOSS 1: (5^2 * 2) / raiz de 25", "ops": ["10", "20", "5"], "c": "10"}
    ]
    m = [
        {"p": "WITHER: raiz de 625 + 2^6 - 10", "ops": ["79", "69", "89"], "c": "79"},
        {"p": "Raiz de (144 + 25) + 3^2", "ops": ["22", "13", "18"], "c": "22"},
        {"p": "Calcula: (2^3 * 3^2) / raiz de 81", "ops": ["8", "12", "6"], "c": "8"},
        {"p": "Portal: alto raiz de 225, ancho raiz de 121. Area?", "ops": ["165", "150", "180"], "c": "165"},
        {"p": "Si 2^x = 128, ¿cuanto vale x?", "ops": ["7", "6", "8"], "c": "7"},
        {"p": "4^3 / 2^4 + raiz de 100", "ops": ["14", "12", "18"], "c": "14"},
        {"p": "BOSS 2: raiz(raiz(1296)) * 2", "ops": ["12", "18", "6"], "c": "12"}
    ]
    d = [
        {"p": "WARDEN: (10^2 - 8^2) / raiz de 9", "ops": ["12", "36", "10"], "c": "12"},
        {"p": "Raiz cubica de 729 + 4^3 - 2^5", "ops": ["41", "51", "31"], "c": "41"},
        {"p": "Calcula: 2^-1 * 100 + raiz de 169", "ops": ["63", "50", "69"], "c": "63"},
        {"p": "Si un Ghast lanza 3^4 bolas y fallas 2^6, ¿acertaste?", "ops": ["17", "21", "27"], "c": "17"},
        {"p": "Raiz de 441 + raiz de 484", "ops": ["43", "45", "41"], "c": "43"},
        {"p": "(raiz de 1024 / 4) * 3", "ops": ["24", "32", "18"], "c": "24"},
        {"p": "FINAL: 1^100 + 0^5 - (raiz de 1)", "ops": ["0", "1", "100"], "c": "0"}
    ]
    
    # Aleatoriedad total
    random.shuffle(f); random.shuffle(m); random.shuffle(d)
    st.session_state.preguntas = f + m + d
    
    # Mezclamos las opciones de cada pregunta
    for p in st.session_state.preguntas:
        random.shuffle(p["ops"])
        
    st.session_state.score = 0
    st.session_state.current = 0
    st.session_state.boss_active = False
    st.session_state.vidas = 5  # <--- AHORA SON 5 VIDAS
    st.session_state.game_over = False

# --- LÓGICA DE DERROTA ---
if st.session_state.vidas <= 0:
    st.markdown("<h1>💀 GAME OVER 💀</h1>", unsafe_allow_html=True)
    st.image("https://media.tenor.com/7Yf0L2G1H6sAAAAi/minecraft-death.gif", width=700)
    st.error(f"Has perdido todos tus corazones. Te quedaste en el nivel {st.session_state.current + 1}.")
    if st.button("RESPAWN EN EL INICIO 🔄"):
        del st.session_state.preguntas
        st.rerun()
    st.stop()

# --- INTERFAZ PRINCIPAL ---
curr = st.session_state.current
vidas_visuales = "❤️" * st.session_state.vidas
st.markdown(f"<p class='heart'>{vidas_visuales}</p>", unsafe_allow_html=True)

# --- SISTEMA DE BOSSES ---
if st.session_state.get('boss_active', False):
    boss_data = {
        6: ["⚠️ ENDER DRAGON", "https://media.tenor.com/I8CBI7yIlFsAAAAi/ender-dragon.gif", "ORO"],
        13: ["💀 EL WITHER", "https://media1.tenor.com/m/0C4A0FJB1EQAAAAd/wither-dance.gif", "DIAMANTE"],
        20: ["🕶️ EL WARDEN", "https://media.tenor.com/AAAQv0Hbb5wAAAAi/warden-minecraft-ward.gif", "NETHERITE"]
    }
    nombre, img, material = boss_data[curr]
    st.write(f"## {nombre}")
    st.image(img, width=700)
    if st.button(f"GOLPE FINAL CON {material} ⚔️"):
        st.session_state.boss_active = False
        st.rerun()

# --- SISTEMA DE PREGUNTAS ---
elif curr < len(st.session_state.preguntas):
    q = st.session_state.preguntas[curr]
    if curr < 6: color, espada = "ORO", "https://media.tenor.com/S7_bQqzBXa8AAAAi/terraria.gif"
    elif curr < 13: color, espada = "DIAMANTE", "https://media.tenor.com/AzZN3_XFVCkAAAAi/minecraft-sword.gif"
    else: color, espada = "NETHERITE", "https://media.tenor.com/cf_fWrmI0ywAAAAi/nigerite-sword.gif"
    
    st.title("Math Craft: Hardcore")
    c1, c2 = st.columns([3, 1])
    c1.write(f"**Nivel {curr + 1} de 20** | Puntos: {st.session_state.score}")
    c1.subheader(f"💀 {q['p']} 💀")
    c2.image(espada, width=80)
    
    respuesta = st.radio("Selecciona tu respuesta:", q["ops"], key=f"r{curr}")
    
    if st.button(f"ATACAR CON {color} ⚔️"):
        if respuesta == q["c"]:
            st.success("¡ACIERTO! Sigues con vida.")
            st.session_state.score += 1
        else:
            st.error(f"¡FALLASTE! Perdiste un corazón. La respuesta era {q['c']}")
            st.session_state.vidas -= 1
        
        st.session_state.current += 1
        if st.session_state.current in [6, 13, 20]:
            st.session_state.boss_active = True
        st.rerun()
    st.progress(curr / 20)

# --- VICTORIA ---
else:
    st.balloons()
    st.title("🏆 ¡MAESTRO DEL HARDCORE!")
    st.write(f"Has sobrevivido con {st.session_state.vidas} corazones.")
    st.write(f"Puntuación final: {st.session_state.score}/20")
    if st.button("JUGAR DE NUEVO 🔄"):
        del st.session_state.preguntas
        st.rerun()
