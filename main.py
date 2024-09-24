# import all necessary libraries
import streamlit as st
import pytesseract
from PIL import Image

# title of web applicaion

st.title(" OCR and Document search web application")


def extract_text(image):
    return pytesseract.image_to_string(image, lang="eng")


uploaded_file = st.file_uploader('upload an image file', type=['jpg', 'jpeg', 'png'])

# check if file uploaded or not
if uploaded_file is not None:

    image = Image.open(uploaded_file)

    st.image(image, caption='uploaded image', use_column_width=True)
    extracted_text = extract_text(image)

    st.write('extracted text :')

    st.text_area("", extracted_text, height=200)

    search_term = st.text_input('enter keyword to search')

    if search_term:

        search_result = [line for line in extracted_text.split('\n') if search_term.lower() in line.lower()]

        if search_result:

            st.write(f"search result for{search_term}")

            for result in search_result:
                st.write(result)

        else:
            st.write(f"No matches found for '{search_term}':")
else:

    st.write("Please upload an image to start the OCR process.")
