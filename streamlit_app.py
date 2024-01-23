import streamlit as st
from PIL import Image

# Title
st.title("Streamlit Image Loader")

# File uploader widget
uploaded_file = st.file_uploader("Choose an image...", type="jpg")

# Check if an image is uploaded
if uploaded_file is not None:
    # Read the image
    image = Image.open(uploaded_file)

    # Display the image
    st.image(image, caption="Uploaded Image", use_column_width=True)
    st.write("Classifying...")  # You can add your image processing logic here

