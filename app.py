import streamlit as st
import joblib

# Load the original vectorizer and model
vectorizer = joblib.load("vectorizer.pkl")
model = joblib.load("NLP_model_compressed.pkl")  # or "NLP_model.pkl" if not compressed

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
            # Vectorize the input using the correct training vectorizer
            input_vec = vectorizer.transform([user_input])

            # Predict the language
            prediction = model.predict(input_vec)[0]

            # Optional: language code to name mapping
            lang_map = {
                'en': 'English',
                'fr': 'French',
                'hi': 'Hindi',
                'es': 'Spanish',
                'de': 'German',
                'it': 'Italian',
                'pt': 'Portuguese',
                'nl': 'Dutch',
                # Add more as needed
            }

            lang_name = lang_map.get(prediction, "Unknown")
            st.success(f"✅ Detected Language: **{lang_name}** (`{prediction}`)")

        except Exception as e:
            st.error(f"❌ Error detecting language: {str(e)}")
