import streamlit as st
from json import loads, dumps

st.title("Personal Settings")
st.write("---")
st.header("Reasons Lists")

with open("data.txt") as f:
    data = f.readlines()
    logs = loads(data[0])
    reasonsMoneySpent = loads(data[1])
    reasonsMoneyRecieved = loads(data[2])

"- - -"
st.subheader("Money Spending List")
st.table(reasonsMoneySpent)

st.write("#### Delete An Option - Reasons For Spending Money")
optionToDelete = st.selectbox("Select an option to delete from the list.", reasonsMoneySpent)

if st.button("Delete"):
    reasonsMoneySpent.remove(optionToDelete)

st.write("#### Add An Option")
optionToAdd = st.text_input("Enter New Reason")
if st.button("Append Reason"):
    reasonsMoneySpent.insert(-2, optionToAdd)

"- - -"
st.subheader("Money Recieving List")
st.table(reasonsMoneyRecieved)

st.write("#### Delete An Option")
optionToDelete = st.selectbox("Select an option to delete from the list. ", reasonsMoneyRecieved)

if st.button("Delete "):
    reasonsMoneyRecieved.remove(optionToDelete)

st.write("#### Add An Option")
optionToAdd = st.text_input("Enter New Reason ")
if st.button("Append Reason "):
    reasonsMoneyRecieved.insert(-2, optionToAdd)


# ----------------------------------------| Footer Of File |----------------------------------------
with open("data.txt", 'w') as f:
    f.writelines([dumps(logs) + "\n", dumps(reasonsMoneySpent) + "\n", dumps(reasonsMoneyRecieved)])