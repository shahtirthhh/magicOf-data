import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello streamlit")
st.write("This is a simple text")

df = pd.DataFrame({
    'Name':["Iphone 16 pro","Samsung S24 Ultra","MI X106"],
    'Price':[2340,2200,1600]
})

st.write(df)

chart_data = pd.DataFrame(np.random.randn(20,3),columns=["a","b","c"])
st.line_chart(chart_data)