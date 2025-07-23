import streamlit as st
import openai
import os
from dotenv import load_dotenv
import auth  # archivo auth.py que tú creaste

# Configuración de la página
st.set_page_config(page_title="Resumen IA", page_icon="🧠")

# Cargar la API key
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# Crear la tabla de usuarios si no existe
auth.create_user_table()

# Control de sesión
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "username" not in st.session_state:
    st.session_state.username = ""
if "logout" not in st.session_state:
    st.session_state.logout = False

# SIDEBAR - Login / Registro
with st.sidebar:
    st.title("🔐 Acceso")
    
    if not st.session_state.logged_in:
        opcion = st.radio("Elige una opción", ["Iniciar sesión", "Registrarse"])

        if opcion == "Registrarse":
            username_reg = st.text_input("Nombre de usuario")
            name_reg = st.text_


