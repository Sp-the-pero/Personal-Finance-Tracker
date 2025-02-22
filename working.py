import streamlit as st
from datetime import datetime
from pytz import timezone
from json import dumps, loads
# from time import sleep

TIMEZONE = timezone("Asia/Karachi")
currentDay = datetime.now(TIMEZONE).strftime("%A") # Monday
currentTime = datetime.now(TIMEZONE).strftime("%I:%M %p") # 11:05 PM
currentDate = datetime.now(TIMEZONE).strftime("%d/%b/%Y") # 04/Nov/2024

def calcWallet():
    global wallet
    wallet = 0
    for i, money in enumerate(datatable['Money']):
        try:
            amount = int(datatable["Amount"][i])
            if money == "Spent":
                wallet -= amount
            elif money == "Recieved":
                wallet += amount
            elif money == "Base":
                wallet = amount
        except ValueError:
            continue

try:
    with open("data.txt") as f:
        data = f.readlines()
        datatable = loads(data[0])
        reasonsMoneySpent = loads(data[1]) 
        reasonsMoneyRecieved = loads(data[2])
        MoneyAmountList = loads(data[3])

except FileNotFoundError:
    # wallet = 0
    datatable = {
        "Money": ["-"],
        "Amount": ["-"],
        "Reason": ["-"],
        "Day": ["-"],
        "Date": ["-"],
        "Time": ["-"]
    }
    reasonsMoneySpent = ["Other"]
    reasonsMoneyRecieved = ["Other"]
    MoneyAmountList = ["Other"]

calcWallet()

# st.write(type(datatable))
# ----------------------------------------| Start Of UI |------------------------------------------
st.title("Personal Expense Tracker App")

col1, col2, col3 = st.columns(3, gap='large')
with col1:
    st.subheader("Table")
with col2:
    st.button("Refresh")
with col3:
    with st.container(border=True, height=50):
        st.write(f"##### Wallet: Rs. {wallet}")

st.table(datatable)

# |------------------------------------ Now the Input Sections xD -------------------------------------|
st.markdown("- - -")
st.subheader("Add New Record")

money = st.selectbox("Enter the money change that occured",["Recieved","Spent","Base"])

amount = st.selectbox("Select the amount of money", MoneyAmountList)

amount = amount if amount != "Other" else st.number_input("Enter the amount of money manually")


reasonsList = reasonsMoneyRecieved if money == "Recieved" else reasonsMoneySpent
if money!="Base":
    reason = st.selectbox("Enter the Reason", reasonsList)
    reason = reason if reason != "Other" else st.text_input("Enter the Reason")
else:
    reason="     "

timeInput = st.selectbox("Select the time", ["Morning (Fajr - 12:00 Noon)", "Afternoon (12:01 PM - Asr)","Evening (Asr - Esha)", "Night (Esha - 12:00 AM)", "Midnight (12:00 Noon - Fajr)"])

st.write("**Time:** ", currentTime)
st.write("**Day:** ", currentDay)
st.write("**Date:** ", currentDate)

if st.button("Add Record"):
    datatable["Money"].append(money)
    # datatable["Money"]
    datatable["Amount"].append(amount)
    datatable["Reason"].append(reason)
    datatable["Day"].append(currentDay)
    datatable["Date"].append(currentDate)
    datatable["Time"].append(timeInput)
    calcWallet()
    pass

# |---------------------------------------- Record Deleter -----------------------------------------|
st.write("- - -")

st.subheader("Delete A Record")

if len(datatable["Money"]) == 1:
    st.warning("Only one record present, pressing the button would delete it automatically.")
    rowNum = 0  # Automatically selects the only available record.
elif len(datatable["Money"]) != 0:
    rowNum = st.slider("Enter the index of record (from the table)", 0, len(datatable["Money"]) - 1)

if len(datatable["Money"]) == 0:
    st.error("No data available to delete.")
else:
    if st.button("Delete Record"):
        for key in datatable:
            datatable[key].pop(rowNum)
        calcWallet()


# ----------------------------------------| Footer Of File |----------------------------------------
with open("data.txt", "w") as f:
    f.writelines([dumps(datatable) + "\n", dumps(reasonsMoneySpent) + "\n", dumps(reasonsMoneyRecieved) + "\n", dumps(MoneyAmountList)])