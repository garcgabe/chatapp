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


write_tab = st.tabs(['write-back'])

with write_tab:
    reflection = st.text_area("speak here")
    if st.button("send text"):
        x = "y"


