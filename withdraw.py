import streamlit as st

st.title("💸 Withdraw Money")

if "current_user" in st.session_state:
    user = st.session_state.users_db[st.session_state.current_user]

    withdraw_amount = st.number_input("Enter amount to withdraw", min_value=1, step=100)
    if st.button("Withdraw"):
        if withdraw_amount <= user["balance"]:
            user["balance"] -= withdraw_amount
            st.success(f"Withdrawal Successful! New Balance: KSh {user['balance']}")
        else:
            st.error("Insufficient funds.")
else:
    st.warning("Please register first.")

st.sidebar.page_link("main.py", label="🏠 Back to Home")

