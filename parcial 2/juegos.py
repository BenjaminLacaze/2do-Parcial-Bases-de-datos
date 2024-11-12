import pandas as pd
import numpy as np
import streamlit as st
from random import randint
# Leer el archivo CSV
df_venta_juegos = pd.read_csv("game_sales_data.csv")

# tabla juegos
df_juego = pd.DataFrame()
df_juego["Ranking"] = df_venta_juegos["Rank"]
df_juego["Juego"] = df_venta_juegos["Name"]
df_juego["Puntuacion Critica"] = df_venta_juegos["Critic_Score"].astype(float)
df_juego["Puntuacion Usuarios"] = df_venta_juegos["User_Score"].astype(float)
df_juego["Ventas Totales"] = df_venta_juegos["Total_Shipped"].astype(float)
df_juego["Anio"] = df_venta_juegos["Year"]
df_juego["Plataforma"] = df_venta_juegos["Platform"]
df_juego["nombre_editor"] = df_venta_juegos["Publisher"]
df_juego["Desarrollador"] = df_venta_juegos["Developer"]
df_juego["ID"] = range(1, 19601)
st.dataframe(df_juego, use_container_width=True, hide_index=True)
#-----------------------------------------------------------------------------------------------------------#

df_desarrollador = pd.DataFrame()

df_desarrollador["Desarrollador"] = list(set(df_venta_juegos["Developer"]))
df_desarrollador["ID_desarrollador"] = range(1,len(df_desarrollador["Desarrollador"])+1)
st.dataframe(df_desarrollador, use_container_width=True, hide_index=True)

#-----------------------------------------------------------------------------------------------------------#

df_editor = pd.DataFrame()

df_editor["nombre_editor"] = list(set(df_venta_juegos["Publisher"]))
df_editor["ID_editor"] = range(1,len(df_editor["nombre_editor"])+1)
st.dataframe(df_editor, use_container_width=True, hide_index=True)

#-----------------------------------------------------------------------------------------------------------#

df_plataforma = pd.DataFrame()

df_plataforma["Plataforma"] = list(set(df_venta_juegos["Platform"]))
df_plataforma["ID_plataforma"] = range(1,len(df_plataforma["Plataforma"])+1)
st.dataframe(df_plataforma, use_container_width=True, hide_index=True)

#-----------------------------------------------------------------------------------------------------------#

df_relacion = pd.merge(df_juego, df_editor[["nombre_editor","ID_editor"]],on="nombre_editor", how="inner")
df_relacion = pd.merge(df_relacion, df_desarrollador[["Desarrollador","ID_desarrollador"]],on="Desarrollador", how="inner")
df_relacion = pd.merge(df_relacion, df_plataforma[["Plataforma","ID_plataforma"]],on="Plataforma", how="inner")

df_relacion = df_relacion.drop(["nombre_editor","Desarrollador","Plataforma"], axis=1)
df_relacion["Puntuacion Critica"] = df_relacion["Puntuacion Critica"].fillna(0)
df_relacion["Puntuacion Usuarios"] = df_relacion["Puntuacion Usuarios"].fillna(0)
df_relacion["Ventas Totales"] = df_relacion["Ventas Totales"].fillna(0)

# Mostrar el DataFrame en Streamlit
st.dataframe(df_relacion, hide_index=True)
