import streamlit as st
import pandas as pd
import numpy as np

st.title("Hello StreamLit!")

## Display Simple texts

st.write("This is a simple text")

## display create a simple dataframe

df = pd.DataFrame({
    'first_col' : [1,2,3,4],
    'second_col' : ['A' , 'B' , 'C' , 'D']
})

## Display the dataframe
st.write("Here is the DataFrame")
st.write(df)

## create line chart
chart_data = pd.DataFrame(
    np.random.randn(20 , 3) , columns = ['a' , 'b' , 'c']
)
st.line_chart(chart_data)