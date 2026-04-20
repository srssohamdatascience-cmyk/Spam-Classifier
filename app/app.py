import sys
import os
import nltk
nltk.download('punkt')
# Fix import path
sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

import streamlit as st
from src.predict import predict_message


st.title('Spam Message Classifier')

st.markdown("---")

user_input = st.text_area("Enter your text here")

if st.button("Predict"):
    if user_input.strip() == "":
        st.warning("Please enter the text")
    else:
        try:
            result = predict_message(user_input)
            if result == 'Spam':
                st.error("This is Spam Message")
            else:
                st.success("This is Not Spam")
        except Exception as e:
            st.error(f"Error:{e}")
            