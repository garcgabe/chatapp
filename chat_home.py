import streamlit as st
import numpy as np

name = 'gabriel garcia'
ipsum = """Lorem ipsum dolor sit amet, 
consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo 
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
 mollit anim id est laborum."""

#st.sidebar.markdown("tutor")

st.title("welcome to gpt")

left, right = st.columns(2, gap = "medium", )

with left: 
    st.subheader("Human")
    st.write(name)
    st.text(ipsum)

with right:
    st.subheader("GPT")
    st.write("mr. chat")
    st.text(ipsum)