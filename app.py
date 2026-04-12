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
        {"p": "FINAL: Raiz de 625 - 5^2", "ops": ["0", "5", "25"], "c": "0"}
    ]
    st.session_state.preguntas = f + m + d
    st.session_state.score = 0
    st.session_state.current = 0
    st.session_state.boss_active = False

curr = st.session_state.current

if st.session_state.get('boss_active', False):
    if curr == 6:
        st.write("## ⚠️ ¡EL ENDER DRAGON!")
        st.image("https://media.tenor.com/I8CBI7yIlFsAAAAi/ender-dragon.gif", width=700)
        if st.button("DERROTAR CON ORO ⚔️"):
            st.session_state.boss_active = False
            st.rerun()
    elif curr == 13:
        st.write("## 💀 ¡EL WITHER!")
        st.image("https://media1.tenor.com/m/0C4A0FJB1EQAAAAd/wither-dance.gif", width=700)
        if st.button("DERROTAR CON DIAMANTE 💎"):
            st.session_state.boss_active = False
            st.rerun()
    elif curr == 20:
        st.write("## 🕶️ ¡EL WARDEN!")
        st.image("https://media.tenor.com/AAAQv0Hbb5wAAAAi/warden-minecraft-ward.gif", width=700)
        if st.button("ESCAPE CON NETHERITE 🔥"):
            st.session_state.boss_active = False
            st.rerun()

elif curr < len(st.session_state.preguntas):
    q = st.session_state.preguntas[curr]
    if curr < 6: btn, img = "ORO", "https://media.tenor.com/S7_bQqzBXa8AAAAi/terraria.gif"
    elif curr < 13: btn, img = "DIAMANTE", "https://media.tenor.com/AzZN3_XFVCkAAAAi/minecraft-sword.gif"
    else: btn, img = "NETHERITE", "https://media.tenor.com/cf_fWrmI0ywAAAAi/nigerite-sword.gif"
    
    st.title("Minecraft Math")
    col1, col2 = st.columns([3, 1])
    col1.write(f"Pregunta {curr + 1}/20")
    col1.subheader(q["p"])
    col2.image(img, width=70)
    
    ans = st.radio("Respuesta:", q["ops"], key=f"r{curr}")
    if st.button(f"ATACAR CON {btn} ⚔️"):
        if ans == q["c"]: st.success("¡Bien!"); st.session_state.score += 1
        else: st.error(f"¡Mal! Era {q['c']}")
        st.session_state.current += 1
        if st.session_state.current in [6, 13, 20]: st.session_state.boss_active = True
        st.rerun()
    st.progress(curr / 20)
else:
    st.balloons()
    st.title("🏆 ¡GANASTE!")
    st.write(f"Puntos: {st.session_state.score}/20")
    if st.button("REINICIAR"):
        st.session_state.current = 0
        st.session_state.score = 0
        st.session_state.boss_active = False
        st.rerun()
