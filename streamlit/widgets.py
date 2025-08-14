import streamlit as st
import pandas as pd

st.title("Text Input from the user")

## Text Input from the user
name = st.text_input("Enter your name: ")

## Slider
age = st.slider("Select your age: " , 0 , 100 , 20)
st.write(f"Your age is {age}")

## Choice selection

options = ["Python" , "C++" , "Golang" , "Java" , "Javascript"]
choice = st.selectbox("Choose your preffered language: " , options)
st.write(f"You have chosen {choice}")

# upload
upload_file = st.file_uploader("Choose a file: " , type = "csv")

if upload_file is not None:
    df = pd.read_csv(upload_file)
    st.write(df.head())

# if name:
#     st.write(f"Hello {name}")
