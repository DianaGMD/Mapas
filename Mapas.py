#Mapas
import streamlit as st
import pandas as pd
import numpy as np

print("Mapa de mi ubicación")
map_data = pd.DataFrame(
    np.random.randn(1000,2) / [50, 50] + [20.613272, -100.401832],
    columns=['lat', 'lon']
)

st.dataframe(map_data)
st.map(map_data)
