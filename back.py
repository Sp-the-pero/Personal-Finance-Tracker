import streamlit as st

st.title("Data At The Backend")
# st.session_state

# Display the datatable from session_state
if "datatable" in st.session_state:
    st.write(st.session_state.datatable)
else:
    st.write("No data available.")
