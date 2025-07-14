import streamlit as st
import joblib

# Load vectorizer and model separately
vectorizer = joblib.load("vectorizer.pkl")
model = joblib.load("NLP_model_compressed.pkl")

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
            prediction = model.predict(input_vec)[0]

            # Optional: show readable name
            lang_map = {
                'en': 'English',
                'fr': 'French',
                'hi': 'Hindi',
                'es': 'Spanish'
            }
            lang_name = lang_map.get(prediction, "Unknown")
            st.success(f"✅ Detected Language: {lang_name} (`{prediction}`)")

        except Exception as e:
            st.error(f"❌ Error detecting language: {str(e)}")
