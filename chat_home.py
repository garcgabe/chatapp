import streamlit as st
from gtts import gTTS 
from playsound import playsound
import openai
openai.organization = st.secrets['OPENAI_ORG']
openai.api_key = st.secrets['OPENAI_API_KEY']

user_message = 'enter an input to receive an output'
bot_message = "no chat sent"
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

st.title("welc to gpt")


with st.chat_message("user"):
    st.write(user_message)

with st.chat_message("assistant"):
    st.write(bot_message)

input_text = st.chat_input("chat here")
if input_text:
    bot_message = call_turbo(input_text, 500)


# left, right = st.columns(2, gap = "medium", )

# with left: 
#     st.subheader("Human")
#     st.write(name)
#     #st.text(ipsum)
#     input_text = st.text_area(label="talk with GPT", height=20)
#     if(st.button("speak")):

#     if st.button("prompt"):
#         response = call_turbo(input_text, 500)
#         st.text(response)


# with right:
#     st.subheader("GPT")
#     st.write("mr\. chat")
#     if type(response) != str:
#         message = response['choices'][0]['message']['content']
#     st.write(message)