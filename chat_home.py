import streamlit as st
# text to speech
from gtts import gTTS 
# playing speech
from playsound import playsound
# GPT calls
import openai
# transcribe audio
import whisper
# record audio
import sounddevice as sd
from scipy.io.wavfile import write

openai.organization = st.secrets['OPENAI_ORG']
openai.api_key = st.secrets['OPENAI_API_KEY']

user_message = 'enter an input to receive an output'
input_text=''
bot_message = "no chat sent"
name = 'gabriel garcia'
ipsum = """Lorem ipsum dolor sit amet, 
consectetur adipiscing elit, sed do eiusmod tempor incididunt ut labore et dolore magna aliqua. 
Ut enim ad minim veniam, quis nostrud exercitation ullamco laboris nisi ut aliquip ex ea commodo 
consequat. Duis aute irure dolor in reprehenderit in voluptate velit esse cillum dolore eu fugiat 
nulla pariatur. Excepteur sint occaecat cupidatat non proident, sunt in culpa qui officia deserunt
 mollit anim id est laborum."""


### NOTE: Process taken
### 1) take in audio from the user based on button press
### 2) transcribe audio to text and store
### 3) tell user audio was taken in; send it back to them
### 4) send this text to GPT to get response back
### 5) add button to show text of the response
### 6) send back audio of the response


def record_audio():
    sd.InputStream(device=0, channels=1)
    fs = 44100  # Sample rate
    seconds = 10  # Duration of recording

    recording = sd.rec(int(seconds * fs), samplerate=fs, channels=1)
    sd.wait()  # Wait until recording is finished
    # write('output.wav', fs, recording)  # Save as WAV file

    # returns ND Array of float64
    return recording

# Whisper performs speech-to-text
# give it output.wav
def audio_to_text(audio_file):
    model = whisper.load_model("small")
    return model.transcribe(audio_file)

# takes in prompt and sends back response
def call_turbo(prompt, max_tokens=1000):
    response = openai.ChatCompletion.create(
    model = 'gpt-3.5-turbo',
    messages = [
        {"role": "user", "content": prompt}
    ],
    max_tokens = max_tokens
    )
    # parse for text
    return response['choices'][0]['message']['content']


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


# with st.chat_message("user"):
#     st.write(user_message)

# with st.chat_message("assistant"):
#     st.write(bot_message)

# input_text = st.chat_input("chat here")
# if input_text:
#     bot_message = call_turbo(input_text, 500)


left, right = st.columns(2, gap = "medium", )

with left: 
    st.write(name)
    #st.text(ipsum)
    input_text = st.text_area(label="talk with GPT", height=20)
    #if(st.button("speak")):

    if st.button("prompt"):
        bot_message = call_turbo(input_text, 500)
        st.text(bot_message)


with right:
    st.subheader("GPT")
    if type(bot_message) != str:
        message = bot_message
    st.write(message)