import streamlit as st
import time
import base64
from PIL import Image


f = open("names.txt","a")

st.set_page_config(page_title="Saran's Demo",layout="wide")
st.title("Welcome to Saran Demo")

with st.container():
    user_name = st.text_input("Enter your name")


dict1 = {"raja": "VP of SW Engineering",
         "guru" : "Cloud QA Manager",
         "sushil": "DC Switching",
         "sankar": "Dev Manager",
         "richard":"QA Manager",
         "karthik": "VP of SW Engineering",
         "john powell": "Director of SW Engineering"}
   
    

count = 0

with st.container():
    if st.button("submit"):
        #if user_name.lower() in dict1:
            #st.write(dict1[user_name])
        #count = count +1
        f.write(user_name + "\n")
        if user_name in dict1:
            st.header(f" Welcome {user_name.capitalize()}-----{dict1[user_name]}")
        else:
            st.header(f"Welcome {user_name.capitalize()}")
        st.write(f" Its my pleasure to have you ")
        st.balloons()
        time.sleep(15)
        st.balloons()
        #time.sleep(10)
        #st.balloons()
        #st.write(count)
        

with st.sidebar:

    st.header("Field of Expertise")
    #st.write("1. Networking")
    #st.write("SDLC", "STLC")
    #st.write("2. ML/AI")

    st.slider("Networking", min_value=1, max_value=10,value=8)
    st.slider("Application Development", min_value=1, max_value=10, value=7)
    st.slider("AI/ML", min_value=1, max_value=10, value=7)

   # st.subheader("Github")
    #st.write("https://github.com/sarannetworkprogammer")
    #st.subheader("LinkedIn")
    #image = Image.open('linkedin.png')
    #st.image(image, caption='Sunrise by the mountains')
    #st.write("https://www.linkedin.com/in/saran-m-6384a299/")
  

    #st.subheader("Tech stack")
    #st.write("C")
    #st.write("Python")
    #st.write("Django")
        
    #with st.container():
    #image = Image.open('linkedin.png')
    #st.image(image, caption='Sunrise by the mountains')
