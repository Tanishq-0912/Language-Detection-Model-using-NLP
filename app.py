import streamlit as st
from joblib import load

# Load the compressed pipeline model
detect_language = load("NLP_model_compressed.pkl")

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
            # Predict using the loaded pipeline
            prediction = detect_language.predict([user_input])[0]

            # Optional: map language codes to names
            lang_map = {
                'en': 'English',
                'fr': 'French',
                'es': 'Spanish',
                'hi': 'Hindi',
                'de': 'German',
                'it': 'Italian',
                'pt': 'Portuguese',
                # Add more if needed
            }

            lang_name = lang_map.get(prediction, "Unknown")
            st.success(f"✅ Detected Language: **{lang_name}** (`{prediction}`)")

        except Exception as e:
            st.error(f"❌ Error detecting language: {str(e)}")
