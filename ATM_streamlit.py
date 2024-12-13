import streamlit as st
st.title("Welcome to ABC Bank")
if 'account_bal' not in st.session_state:
    st.session_state.account_bal = 10000
if 'count' not in st.session_state:
    st.session_state.count = 0
if 'authenticated' not in st.session_state:
    st.session_state.authenticated = False
def deposit():
    depo = st.number_input("Enter the amount to be deposited", min_value=1, step=1, key="deposit_input")
    if st.button("Confirm Deposit"):
        if depo < 100:
            st.error("Minimum deposit amount should be 100")
        elif depo % 100 != 0:
            st.error("Amount should be a multiple of 100")
        elif depo > 50000:
            st.error("Maximum deposit amount is 50000")
        else:
            st.session_state.account_bal += depo
            st.success(f"Your balance after deposit is {st.session_state.account_bal}")
def withdraw():
    if st.session_state.count >= 3:
        st.error("Transaction limit is 3 times")
        return
    withdrawal = st.number_input("Enter the amount to withdraw", min_value=1, step=1, key="withdraw_input")
    if st.button("Confirm Withdrawal"):
        if st.session_state.account_bal < 500:
            st.error("Insufficient balance")
        elif withdrawal < 100:
            st.error("Minimum amount to withdraw is 100")
        elif withdrawal % 100 != 0:
            st.error("Amount should be a multiple of 100")
        elif withdrawal > st.session_state.acbal:
            st.error("Withdraw amount should be less than account balance")
        elif withdrawal > 20000:
            st.error("Transaction amount limit is 20000")
        else:
            st.session_state.acbal -= withdrawal
            st.session_state.count += 1
            st.success(f"Your balance after withdrawal is {st.session_state.account_bal}")
def balance():
    st.success(f"Your current balance is {st.session_state.account_bal}")
def validate():
    if not st.session_state.authenticated:
        pin = st.number_input("Enter your PIN number", min_value=1, step=1, key="pin_input")
        if st.button("Validate PIN"):
            if pin == 1234:
                st.session_state.authenticated = True
                st.success("Authentication successful!")
            else:
                attempts = st.session_state.get("attempts", 3)
                attempts -= 1
                st.session_state["attempts"] = attempts
                if attempts <= 0:
                    st.error("Card blocked")
                    st.stop()
                else:
                    st.error(f"Invalid PIN. Attempts left: {attempts}")

def view_options():
    st.subheader("Select an option")
    option = st.radio("Choose an action:", ("Deposit", "Withdraw", "Balance", "Exit"))

    if option == "Deposit":
        deposit()
    elif option == "Withdraw":
        withdraw()
    elif option == "Balance":
        balance()
    elif option == "Exit":
        st.success("Exiting")
        st.stop()
if not st.session_state.authenticated:
    validate()
else:
    view_options()