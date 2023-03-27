import streamlit as st
import pandas as pd
from datetime import datetime 
import matplotlib.pyplot as plt


st.sidebar.image('Images/finweb.png')
# Introducción personalizada en HTML
intro_html = """
    <div style="background-color:#f5f5f5;padding:10px;border-radius:10px">
        <h1 style="text-align:center">Somos COVENAR</h1>
        <h3 style="text-align:center">Consultora Data Science</h3>
        <p style="text-align:center">Utilizamos el análisis exhaustivo de los datos y las herramientas tecnológicas más avanzadas para un mejor servicio</p>
        <p style="text-align:center">Nuestro objetivo es solucionar problemáticas del mundo de la salud en cuestiones de gestión y recursos hospitalarios</p>
    </div>
"""

# Mostrar la introducción personalizada en la página
st.markdown(intro_html, unsafe_allow_html=True)

#Mediante los datos proporcionados nuestra Consultora eligió Kpis para definir estrategias seguir el cumplimiento de las metas 

#
