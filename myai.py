import os
import google.generativeai as ai
import streamlit as st
os.environ['GOOGLE_API_KEY']="AIzaSyAqtRmOxpAqDC1NRV0T-2M2TxQqazgImQ0"
ai.configure(api_key=os.environ['GOOGLE_API_KEY'])
model=ai.GenerativeModel('gemini-pro')
st.title("Welcome to Amit's GPT")
question=st.text_area('Please enter your questions',"type your question!!!!")

# print(response.prompt_feedback)
# print(response.text)
if st.button("Ask Amit"):
    if (len(question)==0):
        st.warning("Please enter a question")
    else:
        response=model.generate_content(question)
        st.success(response.text)







