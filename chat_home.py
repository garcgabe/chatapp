import streamlit as st
import numpy as np

name = 'gabriel garcia'


#st.sidebar.markdown("tutor")

st.title("welcome to gpt")

left, right = st.columns(2, gap = "medium", )

with left: 
    st.subheader("Human")
    st.write(name)
    st.subheader("response:")

with right:
    st.subheader("GPT")
    st.write("mr. chat")
    st.subheader