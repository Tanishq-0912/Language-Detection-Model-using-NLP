import streamlit as st
import joblib

# Load vectorizer and model separately
vectorizer = joblib.load("vectorizer.pkl")
#model = joblib.load("NLP_model_compressed.pkl")
detect_language = joblib.load("NLP_model_compressed.pkl")

st.set_page_config(page_title="Language Detection App")

st.title("🌐 Language Detection Using NLP")
st.write("Enter text below to detect the language:")

user_input = st.text_area("Text Input", height=150)

if st.button("Detect Language"):
    if user_input.strip() == "":
        st.warning("Please enter some text.")
    else:
        try:
            # First vectorize the input
            input_vec = vectorizer.transform([user_input])
            prediction = detect_language.predict(input_vec)[0]

           
           # prediction = detect_language.predict([user_input])[0]
            st.success(f"✅ Detected Language: `{prediction}`")

        except Exception as e:
            st.error(f"❌ Error detecting language: {str(e)}")
