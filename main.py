import streamlit as st
import random

# Simulated user database
if "users_db" not in st.session_state:
    st.session_state.users_db = {}

# Register User
def register_user(name, phone_number):
    user_id = random.randint(1000, 9999)
    st.session_state.users_db[user_id] = {
        "name": name, 
        "phone_number": phone_number, 
        "balance": 0
    }
    return user_id

# UI Design
st.markdown('<h1 style="text-align:center; color:#4CAF50;">💰 M-Pesa Clone</h1>', unsafe_allow_html=True)
st.sidebar.title("📌 Menu")

# User Registration
st.sidebar.subheader("Register")
name = st.sidebar.text_input("Name")
phone_number = st.sidebar.text_input("Phone Number")

if st.sidebar.button("Register"):
    if name and phone_number:
        user_id = register_user(name, phone_number)
        st.sidebar.success(f"User {name} registered with ID {user_id}.")
        st.session_state.current_user = user_id
    else:
        st.sidebar.error("Please enter both name and phone number.")

# Show User Balance
if "current_user" in st.session_state:
    user = st.session_state.users_db[st.session_state.current_user]
    st.markdown(f'<div style="text-align:center; font-size:22px;">'
                f'Hello, {user["name"]} 👋<br>'
                f'Your Balance: <span style="color:#4CAF50;">KSh {user["balance"]}</span></div>',
                unsafe_allow_html=True)

# Sidebar Navigation
st.sidebar.page_link("pages/deposit.py", label="💵 Deposit Money")
st.sidebar.page_link("pages/withdraw.py", label="💸 Withdraw Money")
st.sidebar.page_link("pages/cash_pickup.py", label="🏦 Request Cash Pickup")

