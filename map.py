import streamlit as st 
import numpy as np
import pandas as pd 

map_data = pd.DataFrame(
    np.random.randn(1000, 2) / [100, 100] + [18.857097, -97.111848],
    columns=['lat', 'lon']
)
st.map(map_data)