import streamlit as st
from json import loads, dumps

st.title("Personal Settings ")
st.write("---")
st.header("1. Reasons Lists")
# ":material-settings:"
with open("data.txt") as f:
    data = f.readlines()
    logs = loads(data[0])
    reasonsMoneySpent = loads(data[1])
    reasonsMoneyRecieved = loads(data[2])
    MoneyAmountList = loads(data[3])

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

# ----------------------------------------| Money List |----------------------------------------
st.write("---")
st.header("2. Money Amount List")

st.table(MoneyAmountList)

st.write("#### Delete An Option")
optionToDelete = st.selectbox("Select an option to delete from the list.  ", MoneyAmountList)

if st.button("Delete  "):
    MoneyAmountList.remove(optionToDelete)

st.write("#### Add An Option")
optionToAdd = st.text_input("Enter New Reason  ")
if st.button("Append Reason  "):
    MoneyAmountList.insert(-2, optionToAdd)


# ----------------------------------------| Footer Of File |----------------------------------------
with open("data.txt", 'w') as f:
    f.writelines([dumps(logs) + "\n", dumps(reasonsMoneySpent) + "\n", dumps(reasonsMoneyRecieved) + "\n", dumps(MoneyAmountList)])