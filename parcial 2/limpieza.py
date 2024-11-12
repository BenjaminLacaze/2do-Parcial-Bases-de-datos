import pandas as pd
import numpy as np
from random import randint
import streamlit as st

df_venta_juegos = pd.read_csv("game_sales_data.csv")
lista_desarrollador = list(set(df_venta_juegos["Developer"]))
df_desarrollador = pd.DataFrame()
df_desarrollador["Desarrollador"] = pd.DataFrame(lista_desarrollador)
df_desarrollador["ID"]=range(1,len(df_venta_juegos["Developer"]+1))
st.dataframe(df_desarrollador, use_container_width=True, hide_index=True)
st.write(df_desarrollador)