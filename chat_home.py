import streamlit as st
import numpy as np

st.sidebar.markdown("tutor")

st.title("welcome to gpt")

left, right = st.columns(2, gap = "medium")

with left: 
    st.subheader("you")
    st.write("gabe")
    st.subheader("response:")

with right:
    st.subheader("gpt")
    st.write("mr. chat")