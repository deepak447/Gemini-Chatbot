import streamlit as st
import google.generativeai as genai
from dotenv import load_dotenv
import os
import time
load_dotenv()

# configuration strealit page setting

st.set_page_config(
    page_title = "chat with gemini-pro",
    page_icon=":brain:", #favicon emoji
    layout= "centered" # page layoutf
)
# generation_config = {
#   "temperature": 1,
#   "top_p": 0.95,
#   "top_k": 64,
#   "max_output_tokens": 8192,
 
# }
safety_settings = [
  {
    "category": "HARM_CATEGORY_HARASSMENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_HATE_SPEECH",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_SEXUALLY_EXPLICIT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
  {
    "category": "HARM_CATEGORY_DANGEROUS_CONTENT",
    "threshold": "BLOCK_MEDIUM_AND_ABOVE",
  },
]
# set up google gemini -pro AI model
genai.configure(api_key = os.environ['GOOGLE_API_KEY'])
model = genai.GenerativeModel(model_name="gemini-1.0-pro",safety_settings=safety_settings)
# funtion to translate roles b/w gemini pro and and streamlit terminology

def translate_role(user_role):
    if user_role =="model":
        return 'assistant'
    else:
        return user_role
    
# initialize chat session in streamlit if not already persent 
    
if "chat_session" not in st.session_state:
    st.session_state.chat_session = model.start_chat(history=[])

# display the chatbot
    
st.markdown("""<h1 style= "text-align: center;"> 
            <span style="color: blue;">Gemini </span>
        <span style="color: red;">Chat</span>
        <span style="color: green;">bot</span>
            </h1>""",unsafe_allow_html=True)

# display chat history

for message in st.session_state.chat_session.history:
    with st.chat_message(translate_role (message.role)):
        st.markdown(message.parts[0].text)

# input field for user's message
        
question = st.chat_input("ask to gemini")

if question:
    # add user massage in chat display
    st.chat_message('user').markdown(question)
    #send user message to gemini and get respose
    gemini_response = st.session_state.chat_session.send_message(question)


    # Display assistant response in chat message container
    with st.chat_message("assistant"):
        response = st.write(gemini_response.text)

    