import streamlit as st

st.title("💵 Deposit Money")

if "current_user" in st.session_state:
    user = st.session_state.users_db[st.session_state.current_user]

    deposit_amount = st.number_input("Enter amount to deposit", min_value=1, step=100)
    if st.button("Deposit"):
        user["balance"] += deposit_amount
        st.success(f"Deposit Successful! New Balance: KSh {user['balance']}")
else:
    st.warning("Please register first.")

st.sidebar.page_link("main.py", label="🏠 Back to Home")


