import streamlit as st
import time


dict1 = {"raja": "VP of SW Engineering",
         "guru" : "Cloud QA Manager",
         "sushil": "DC Switching",
         "sreenath": "automation",
         "sankar": "Hotpatch",
         "sona": "Director of SW engineering",
                                        
                                        }
f = open("sample.txt","a")

st.set_page_config(page_title="Saran",layout="wide")
st.title("Welcome to Saran")

with st.container():
    user_name = st.text_input("Enter your name")

    if user_name in dict1:
        st.write(dict1[user_name])
    



with st.container():
    if st.button("submit"):
        f.write(user_name + "\n")
        st.write("Thanks for visiting  {user_name} me")
        

with st.container():
    st.sidebar.title("Thanks for stopping BY")
    


""" 
with st.container():
    st.selectbox()

 """
