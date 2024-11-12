import pandas as pd
import numpy as np
import streamlit as st
from random import randint

df_venta_juegos = pd.read_csv("game_sales_data.csv")

# Crear una lista única de desarrolladores



df_desarrollador = pd.DataFrame()

df_desarrollador["Desarrollador"] = list(set(df_venta_juegos["Developer"]))
df_desarrollador["ID_desarrollador"] = range(1,len(df_desarrollador["Desarrollador"]))
st.dataframe(df_desarrollador, use_container_width=True, hide_index=True)
# Mostrar el DataFrame en Streamlit

st.write(df_desarrollador)


