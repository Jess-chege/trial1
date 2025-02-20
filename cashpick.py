import streamlit as st
import random
import time

st.title("🏦 Request Cash Pickup")

# Simulated cash pickup function
def request_cash_pickup(user, amount):
    time.sleep(2)  # Simulate delay
    success = random.choice([True, False])
    if success:
        user["balance"] += amount
        return f"✅ Cash pickup successful! New Balance: KSh {user['balance']}"
    return "❌ Pickup failed. Please try again later."

if "current_user" in st.session_state:
    user = st.session_state.users_db[st.session_state.current_user]

    amount = st.number_input("Enter amount for pickup", min_value=1, step=100)
    if st.button("Request Pickup"):
        response = request_cash_pickup(user, amount)
        st.info(response)
else:
    st.warning("Please register first.")

st.sidebar.page_link("main.py", label="🏠 Back to Home")


