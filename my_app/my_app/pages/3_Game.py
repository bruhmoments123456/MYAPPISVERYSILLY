import streamlit as st
import random

st.title("🎮 Game đoán số")

if "secret" not in st.session_state:
    st.session_state.secret = random.randint(1, 100)
    st.session_state.tries = 0

guess = st.number_input("Đoán số", 1, 100)

if st.button("Đoán"):
    st.session_state.tries += 1
    if guess < st.session_state.secret:
        st.warning("Lớn hơn")
    elif guess > st.session_state.secret:
        st.warning("Nhỏ hơn")
    else:
        st.success(f"Đúng sau {st.session_state.tries} lần!")

if st.button("Chơi lại"):
    st.session_state.secret = random.randint(1, 100)
    st.session_state.tries = 0
