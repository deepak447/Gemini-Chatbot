import streamlit as st
from dotenv import load_dotenv
import google.generativeai as genai
import os
from PIL import Image

genai.configure(api_key=os.environ['GOOGLE_API_KEY'])

# function to get response from the gemini 
def get_gemini_response(question,image):
    model = genai.GenerativeModel('gemini-pro-vision')
    if input != '':
        response = model.generate_content([question,image])
    else:
        response = model.generate_content(image)
    return response.text

st.set_page_config(page_title='gemini_image',page_icon='🔎')
st.markdown("""
    <h1 style="text-align: center;">
        <span style="color: blue;">G</span>
        <span style="color: red;">e</span>
        <span style="color: green;">m</span>
        <span style="color: blue;">i</span>
        <span style="color: green;">n</span>
        <span style="color: red;">i</span>
             &nbsp;&nbsp;&nbsp;&nbsp; <span style="color: #FF5733;">A</span>
         <span style="color: #3498DB;">p</span>
         <span style="color: #F4D03F;">p</span>
         <span style="color: #2ECC71;">l</span>
         <span style="color: #9B59B6;">i</span>
         <span style="color: #E74C3C;">c</span>
         <span style="color: #1ABC9C;">a</span>
         <span style="color: #D35400;">t</span>
         <span style="color: #34495E;">i</span>
         <span style="color: #F39C12;">o</span>
         <span style="color: #8E44AD;">n</span>
    </h1>
""", unsafe_allow_html=True)

input = st.text_input('Input Prompt',key='input')

uploaded_file = st.file_uploader('Choose an Image..,',type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image,caption='uploaded image',use_column_width= True)

submit = st.button('Click it..')

if submit:
    response = get_gemini_response(input,image)
    st.write(response)
