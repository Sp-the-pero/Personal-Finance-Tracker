import streamlit as st
from datetime import datetime
from pytz import timezone

TIMEZONE = timezone("Asia/Karachi")
currentDay = datetime.now(TIMEZONE).strftime("%A") # Monday
currentTime = datetime.now(TIMEZONE).strftime("%I:%M %p") # 11:05 PM
currentDate = datetime.now(TIMEZONE).strftime("%d/%b/%Y") # 04/Nov/2024

if "wallet" not in st.session_state:
    st.session_state.wallet = 0

# wallet = 0
def calcWallet():
    st.session_state.wallet = 0
    for i, money in enumerate(st.session_state.datatable["Money"], start=0):
        try:
            amount = int(st.session_state.datatable["Amount"][i])
        except ValueError:
            continue
        
        # obal st.session_state.wallet
        if money == "Spent":
            st.session_state.wallet -= amount
        else:
            st.session_state.wallet += amount



if "datatable" not in st.session_state:
    st.session_state.datatable = {
        "Money": ["-"],
        "Amount": ["-"],
        "Reason": ["-"],
        "Day": ["-"],
        "Date": ["-"],
        "Time": ["-"]
    }

# st.write(type(datatable))
st.title("Personal Expense Tracker App")

col1, col2 = st.columns(2, gap='large')
with col1:
    st.subheader("Table")
with col2:
    with st.container(border=True, height=50):
        st.write(f"##### Wallet: Rs. {st.session_state.wallet}")

st.table(st.session_state.datatable)

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
    st.session_state.datatable["Money"].append(money)
    # datatable["Money"]
    st.session_state.datatable["Amount"].append(amount)
    st.session_state.datatable["Reason"].append(reason)
    st.session_state.datatable["Day"].append(currentDay)
    st.session_state.datatable["Date"].append(currentDate)
    st.session_state.datatable["Time"].append(timeInput)
    calcWallet()
    pass

# |---------------------------------------- Record Deleter -----------------------------------------|
st.write("- - -")

st.subheader("Delete A Record")

rowNum = st.slider("Enter the index of record (from the table)", 0, len(st.session_state.datatable["Money"]))
if st.button("Delete Record"):
    calcWallet()
    for key in st.session_state.datatable:
        st.session_state.datatable[key].pop(rowNum)