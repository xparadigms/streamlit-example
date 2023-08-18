import streamlit as st
import requests
import json

# Load configuration from TOML file

# Extract the API key from the configuration
deepl_api_key = st.secrets.deepL.deepl_api_key

# Define the translation function


def translate_with_deepL(text: str):
    url = "https://api-free.deepl.com/v2/translate"
    payload = {"text": text, "target_lang": "KO"}
    headers = {
        "Authorization": f"DeepL-Auth-Key {deepl_api_key}",
        "User-Agent": "YourApp/1.2.3",
        "Content-Type": "application/x-www-form-urlencoded",
    }

    response = requests.post(url, data=payload, headers=headers)

    if response.status_code == 200:
        return response.text
    else:
        return None


# Streamlit app title
st.title("Markdown Translation with DeepL")

# Upload a Markdown file
markdown_file = st.file_uploader("Upload a Markdown file", type=["md"])

if markdown_file is not None:
    markdown_text = markdown_file.read().decode("utf-8")

    # Display uploaded Markdown content
    st.markdown('<div style="background-color: orange; padding: 10px;"><h3  style="color: black;">1. Uploaded Markdown Content</h3></div>',
                unsafe_allow_html=True)
    st.markdown(markdown_text, unsafe_allow_html=True)

    # Edit the uploaded Markdown content
    # st.subheader("Edit Markdown Content")
    # Adjust the height as needed
    st.markdown('<div style="background-color: orange; padding: 10px;"><h3  style="color: black;">2. Edit Markdown Content</h3></div>',
                unsafe_allow_html=True)

    edited_markdown = st.text_area(
        "", markdown_text, height=800)
    st.markdown('<div style="background-color: orange; padding: 10px;"><h3  style="color: black;">3. Translate with DeepL</h3></div>',
                unsafe_allow_html=True)
    st.markdown("")
    # Button to trigger translation
    # HTML button with inline styling for desired appearance

    # Button to trigger translation
    if st.button("Translate with DeepL"):
        # Translate edited Markdown content
        translated_text = translate_with_deepL(edited_markdown)

        # Extract translation result from JSON
        data = json.loads(translated_text)
        translated_result = data['translations'][0]['text']

        # Display translated content
        st.subheader("Translated Content")
        st.markdown(translated_result, unsafe_allow_html=True)
