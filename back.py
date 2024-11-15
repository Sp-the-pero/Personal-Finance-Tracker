import streamlit as st

st.title("Data At The Backend")

try:
    with open("data.txt") as f:
        data = f.readlines()
    st.write(data)
except FileNotFoundError:
    st.write("No data available.")