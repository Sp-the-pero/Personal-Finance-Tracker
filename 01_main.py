import streamlit as st

App = st.Page(
    page="working.py",
    title="App",
    icon="",
    default=True
)


Data = st.Page(
    page="back.py", 
    title="Data"
)

nav = st.navigation([App, Data])

nav.run()