import streamlit as st

App = st.Page(
    page="working.py",
    title="App",
    icon=":material/grid_view:",
    default=True
)

Data = st.Page(
    page="back.py", 
    title="Data",
    icon=":material/database:"
)

Setting = st.Page(
    page="setting.py",
    title="Setting",
    icon=":material/settings:"
)

nav = st.navigation([App, Data, Setting])

nav.run()