import streamlit as st
from datetime import datetime
from pytz import timezone
import json

TIMEZONE = timezone("Asia/Karachi")
currentDay = datetime.now(TIMEZONE).strftime("%A") # Monday
currentTime = datetime.now(TIMEZONE).strftime("%I:%M %p") # 11:05 PM
currentDate = datetime.now(TIMEZONE).strftime("%d/%b/%Y") # 04/Nov/2024

# wallet = 
datatable = {"s": " "}
try:
    with open("data.txt") as f:
        data = f.readlines()
        wallet = int(data[0])
        datatable = json.loads(data[1])
except FileNotFoundError:
    wallet = 0
    datatable = {
        "Money": ["-"],
        "Amount": ["-"],
        "Reason": ["-"],
        "Day": ["-"],
        "Date": ["-"],
        "Time": ["-"]
    }

def calcWallet():
    global wallet
    for i, money in enumerate(datatable["Money"], start=0):
        try:
            amount = int(datatable["Amount"][i])
        except ValueError:
            continue
        
        # obal wallet
        if money == "Spent":
            wallet -= amount
        else:
            wallet += amount

# st.write(type(datatable))
st.title("Personal Expense Tracker App")

col1, col2 = st.columns(2, gap='large')
with col1:
    st.subheader("Table")
with col2:
    with st.container(border=True, height=50):
        st.write(f"##### Wallet: Rs. {wallet}")

st.table(datatable)

# |------------------------------------ Now the Input Sections xD -------------------------------------|
st.markdown("- - -")
st.subheader("Add New Record")

money = st.selectbox("Enter the money change that occured",["Recieved","Spent"])

amount = st.selectbox("Select the amount of money", ["50","100", "Other"])

amount = amount if amount != "Other" else st.number_input("Enter the amount of money manually")

reasonsList = ["Daily Pocket Money", "Weekly Pocket Money", "Other"] if money == "Recieved" else ["French Fries", "Other"]

reason = st.selectbox("Enter the Reason", reasonsList)
reason = reason if "Other" is not reason else st.text_input("Enter the Reason")

timeInput = st.selectbox("Select the time", ["Morning (Fajr - 12:00 Noon)", "Afternoon (12:01 PM - Asr)","Evening (Asr - Esha)", "Night (Esha - 12:00 AM)", "Midnight (Fajr - 12:00 Noon)"])

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

rowNum = st.slider("Enter the index of record (from the table)", 0, len(datatable["Money"]))
if st.button("Delete Record"):
    calcWallet()
    for key in datatable:
        datatable[key].pop(rowNum)

with open("data.txt", "w") as f:
    f.writelines([f"{wallet}\n", json.dumps(datatable)])