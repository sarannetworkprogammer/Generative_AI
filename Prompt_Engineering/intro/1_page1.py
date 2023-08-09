import streamlit as st


def main():

    st.set_page_config(page_title="Saran",layout="wide")

    f = open("problems.txt","a")

    with st.container():

        st.title("Questions/Problem statements")
       
        st.subheader("I'm a software solutions provider, tackling problems head-on with expertise.")

        user_name = st.text_input("Enter your name")
        problem_statement = st.text_area("Question/Problem statement")

        if st.button("Submit"):


            f.write(user_name + ": " +  problem_statement +"\n")

            st.subheader("Thanks a lot for your valuable time. I will get back to you with solution ")
          



if __name__ == "__main__":
    main()



