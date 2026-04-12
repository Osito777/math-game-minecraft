import streamlit as st

st.set_page_config(page_title="Math Craft", page_icon="⚔️")

st.markdown("<style>.main{background-color:#0d0d0d;color:white}button{width:100%}</style>", unsafe_allow_html=True)

if 'preguntas' not in st.session_state:
    f = [
        {"p": "2^4 bloques. Explota R-16, quedan?", "ops": ["12", "8", "4"], "c": "12"},
        {"p": "R-144 por 2", "ops": ["24", "12", "48"], "c": "24"},
        {"p": "3^3 + R-81", "ops": ["36", "30", "27"], "c": "36"},
        {"p": "2^6 slots. Mitad full, quedan?", "ops": ["32", "16", "64"], "c": "32"},
        {"p": "R-cubica 64 + 5^2", "ops": ["29", "21", "24"], "c": "29"},
        {"p": "L1: R-400 / 5", "ops": ["4", "8", "20"], "c": "4"}
    ]
    m = [
        {"p": "WITHER: (2^3)^2 - R-16", "ops": ["60", "32", "64"], "c": "60"},
        {"p": "R- de R-625", "ops": ["5", "25", "10"], "c": "5"},
        {"p": "5^3 o 11^2?", "ops": ["5^3", "11^2", "Iguales"], "c": "5^3"},
        {"p": "R-225 x R-4", "ops": ["30", "15", "60"], "c": "30"},
        {"p": "Portal: alto R-144, ancho R-100. Area?", "ops": ["120", "22", "200"], "c": "120"},
        {"p": "4^3 - 3^4", "ops": ["-17", "17", "7"], "c": "-17"},
        {"p": "L2: Rcub 1000 x 2^3", "ops": ["80", "60", "100"], "c": "80"}
    ]
    d = [
        {"p": "HARD: R-16 x (3^4 / 9)", "ops": ["36", "27", "81"], "c": "36"},
        {"p": "(2^2 x 5^2) - R-144", "ops": ["88", "100", "76"], "c": "88"},
        {"p": "R-169 + R-196 + R-225", "ops": ["42", "30", "45"], "c": "42"},
        {"p": "2^7 / R-64", "ops": ["16", "32", "8"], "c": "16"},
        {"p": "Warden: Rcub 216 + 7^2", "ops": ["55", "49", "60"], "c": "55"},
        {"p": "(10^2 - 8^2) + R-1", "ops": ["37", "36", "19"], "c": "37"},
        {"p": "FINAL: R-625 - 5^2", "ops": ["0", "5", "25"], "c": "0"}
    ]
    st.session_state.preguntas = f + m + d
    st.session_state.score = 0
    st.session_state.current = 0
    st.session_state.boss_active = False

curr = st.session_state.current

if st.session_state.get('boss_active', False):
    if curr == 6:
        st.write("## ⚠️ ENDER DRAGON")
        st.image("https://media.tenor.com/I8CBI7yIlFsAAAAi/ender-dragon.gif", width=700)
        if st.button("ATAQUE ORO ⚔️"):
            st.session_state.boss_active = False
            st.rerun()
    elif curr == 13:
        st.write("## 💀 WITHER")
        st.image("https://media1.tenor.com/m/0C4A0FJB1EQAAAAd/wither-dance.gif", width=700)
        if st.
