import streamlit as st
from password_generator import generate_random_password, generate_pin, generate_memorable_password

import nltk

nltk.download("words")

st.image('images/banner.jpeg')
st.header("⚡ Password Generator")
pass_type = st.radio('Password type',("Random password",'Memorable password', "Pin code"))

if pass_type == 'Random password':

    pass_length = st.slider('Length',5,50) 
    pass_number = st.toggle("Include number")
    pass_symbol = st.toggle("Include symbol")
    password = generate_random_password(pass_length,pass_number,pass_symbol)

if pass_type == 'Pin code':
    pass_length = st.slider('Numbers',5,50)
    password = generate_pin(pass_length)  

if pass_type =="Memorable password":
    pass_length = st.slider('Words',5,50)
    seprator = st.selectbox("Seprator",("-",".",',' ))
    captalize = st.toggle("Captalize")
    password = generate_memorable_password(pass_length,seprator,captalize,nltk.corpus.words.words())



"""
Your password is:

"""
st.code(password)

