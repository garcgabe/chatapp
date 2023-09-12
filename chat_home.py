import streamlit as st
import os
import openai
import whisper
from gtts import gTTS 
from playsound import playsound
import pandas as pd
openai.organization = st.secrets['OPENAI_ORG']
openai.api_key = st.secrets['OPENAI_API_KEY']

response = 'enter an input to receive an output'
name = 'gabriel garcia'
ipsum = """Lorem ipsum dolor sit amet, 
consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo 
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
 mollit anim id est laborum."""


def call_turbo(prompt, max_tokens):
    response = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages = [
        {"role": "user", "content": prompt}
    ],
    max_tokens = max_tokens
    )
    return response

def toSpeech(message, language):
    speech = gTTS(text = message, lang=language)
    speech.save('example.mp3')
    playsound('example.mp3')

#st.sidebar.markdown("tutor")

##
##
##    Beginning of
##    App Frontend
##
##

st.title("welcome to gpt")

left, right = st.columns(2, gap = "medium", )

with left: 
    st.subheader("Human")
    st.write(name)
    st.text(ipsum)
    input_text = st.text_area(label="talk with GPT", height=20)
    if st.button("prompt"):
        response = call_turbo(input_text)

with right:
    st.subheader("GPT")
    st.write("mr. chat")
    st.text(response)