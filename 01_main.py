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

Setting = st.Page(
    page="setting.py",
    title="Setting"
)

nav = st.navigation([App, Data, Setting])

nav.run()