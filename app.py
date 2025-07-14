
import streamlit as st
import pickle

from joblib import load

detect_language = load("NLP_model_compressed.pkl")

# Load the model
# with open("NLP_model.pkl", "rb") as f:
#     detect_language = pickle.load(f)

# Streamlit App
st.set_page_config(page_title="Language Detection App")

st.title("🌐 Language Detection Using NLP")
st.write("Enter text below to detect the language:")

user_input = st.text_area("Text Input", height=150)

if st.button("Detect Language"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:
            language = detect_language(user_input)
            st.success(f"Detected Language Code: `{language}`")
        except Exception as e:
            st.error(f"Error detecting language: {str(e)}")
