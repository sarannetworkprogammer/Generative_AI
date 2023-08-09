import streamlit as st


st.title("welcome to firstapp")

st.sidebar.title("welcome to Intellipat")


user_input = st.text_input("enter the input")
st.button("submit")

st.write(user_input)

st.selectbox("pick your course",["ML","Cloud"])


