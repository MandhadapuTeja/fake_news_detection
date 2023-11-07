import streamlit as st 
import joblib 
st.title("FAKE NEWS DETECTION") 
text_model=joblib.load('fake-real') 
ip=st.text_input("Enter the title: ") 
op=text_model.predict([ip]) 
if st.button('PREDICT'): 
  st.title(op[0]) 