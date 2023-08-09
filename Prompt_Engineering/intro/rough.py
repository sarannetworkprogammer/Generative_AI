import streamlit as st

st.title('Counter Example using Callbacks')
	
if 'count' not in st.session_state:
	st.session_state.count = 0

def increment_counter():
	st.session_state.count += 1

st.button('Submit', on_click=increment_counter)

st.write('Count = ', st.session_state.count)


 st.header("Techstack")
    tab1, tab2, tab3 = st.tabs(["Dev", "Testing", "AI"])

    with tab1:
        st.header("A cat")    
        st.write("Networking")