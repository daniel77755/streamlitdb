import streamlit as st
import requests
import json



# Inicializa variables de sesión
if "feedback" not in st.session_state:
    st.session_state.feedback = None
if "response_shown" not in st.session_state:
    st.session_state.response_shown = False
if "respuesta" not in st.session_state:
    st.session_state.respuesta = ""

col1, col2 = st.columns([3,1])

with col1:
    st.markdown("")  # Espacio vacío para dejar la imagen sola en la fila

with col2:
    st.image("logohabi.png", width=250)

    
# Encabezado centrado con estilo mejorado
st.markdown("""
    <div style='text-align: center; margin-top: 30px; margin-bottom: 20px;'>
        <h1 style='font-family: "Segoe UI", Tahoma, Geneva, Verdana, sans-serif; 
                   color: #4B0082; 
                   font-size: 40px;
                   text-shadow: 1px 1px 2px #7C01FF;'>Agente Radicaciones Habicredit</h1>
        <p style='font-size: 18px; color: #555;'>Consulta y obtén respuestas inteligentes de radicaciones liquidez</p>
    </div>
""", unsafe_allow_html=True)

# Estilos personalizados 
st.markdown("""
    <style>
    /* Estilo general del contenedor de la app */
    .main {
        background-color: #F7F7F9;
    }

    /* Botón de submit */
    .stButton > button {
        background-color: #7C01FF;
        color: white;
        border-radius: 10px;
        padding: 10px 24px;
        border: none;
        font-weight: bold;
        transition: 0.3s ease;
        box-shadow: 0px 4px 10px rgba(124,1,255,0.2);
    }

    .stButton > button:hover {
        background-color: #6200cc;
        color: white;
        box-shadow: 0px 4px 12px rgba(124,1,255,0.4);
    }

    /* Input de texto */
    .stTextInput>div>div>input {
        border: 2px solid #7C01FF;
        border-radius: 8px;
        padding: 10px;
        font-size: 16px;
        box-shadow: 0px 2px 6px rgba(124,1,255,0.15);
        transition: box-shadow 0.3s ease, border 0.3s ease;
    }

    .stTextInput>div>div>input:hover {
        box-shadow: 0px 2px 8px rgba(124,1,255,0.35);
    }

    .stTextInput>div>div>input:focus {
        border: 2px solid #4B0082;
        box-shadow: 0px 2px 10px rgba(75,0,130,0.5);
    }

    /* Centrado de formularios */
    .block-container {
        padding-top: 1rem;
        padding-bottom: 1rem;
    }
    </style>
""", unsafe_allow_html=True)

    
def connect_api(query):
    headers = {
        "x-api-key": "AIzaSyBb2222222-1111111111",
        "Content-Type": "application/json",
        "Origin": "https://mi-app.streamlit.app"
    }
    
    payload = json.dumps({
        "data": {"question": query}
    })

    responses = requests.post("https://agent-gateway-radicaciones-ak877eu7.uc.gateway.dev/streamlit/event", headers=headers, data=payload) 
    return responses 
    
# Usa st.form para agrupar el input y botón 
with st.form(key='chat_form'): 
    query = st.text_input("Realiza las preguntas relacionadas a radicaciones")
    submit_button = st.form_submit_button(label='Responder')      

if submit_button and query:
    response_api = connect_api(query)
    st.session_state.response_shown = False
    st.session_state.score_ready = False
    
    if response_api.status_code != 200:
        st.write("⚠️ Error HTTP:", response_api.status_code)
        st.write("Texto de respuesta:", response_api.text)
        st.write("⚠️ No 'response' key found in JSON.", response_api)
    else:
        st.session_state.respuesta = response_api.text
        st.session_state.response_shown = True

    
