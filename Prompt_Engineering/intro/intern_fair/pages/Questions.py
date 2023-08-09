import streamlit as st

from PIL import Image


def main():

    st.set_page_config(page_title="Saran",layout="wide")

    f = open("problems.txt","a")

    with st.container():

      
       
        st.title("I'm a software solutions provider, tackling problems head-on with expertise.")

        with st.sidebar:

            st.subheader("Questions/Problem statements")
            st.write("Any Questions, Suggestions ,Feedback")
            #st.subheader("Github")
            #st.write("https://github.com/sarannetworkprogammer")
            st.subheader("Resume")
            with st.container():
                image = Image.open('resume.png')
                st.image(image, width=200)

        user_name = st.text_input("Enter your name")
        problem_statement = st.text_area("Question/Problem statement/suggestions")

        if st.button("Submit"):


            f.write(user_name + ": " +  problem_statement +"\n")

            st.subheader("Thanks a lot for your valuable time. I will get back to you with solution ")
        
                
 
          



if __name__ == "__main__":
    main()

