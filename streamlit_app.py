'''import streamlit as st
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
    st.write("Classifying...")  # You can add your image processing logic here'''

'''import streamlit as st
import os

# Title
st.title("Whole Slide Image Viewer")

# File uploader widget
uploaded_file = st.file_uploader("Choose a .svs file...", type="svs")

# Check if an image is uploaded
if uploaded_file is not None:
    # Save the uploaded file locally
    with open("temp.svs", "wb") as f:
        f.write(uploaded_file.getvalue())

    # Use the openslide executable to open and read the WSI
    os.system(f"openslide-show-properties temp.svs")

    # You can add more interactive features or analysis logic here

    # Remove the temporary file
    os.remove("temp.svs")'''

import streamlit as st
import pyvips
from io import BytesIO

# Title
st.title("Whole Slide Image Viewer")

# File uploader widget
uploaded_file = st.file_uploader("Choose a .svs file...", type="svs")

# Check if an image is uploaded
if uploaded_file is not None:
    # Read the image using PyVips
    slide = pyvips.Image.new_from_buffer(uploaded_file.getvalue(), "")

    # Convert to RGB
    rgb_image = slide.colourspace("srgb")

    # Convert to PIL Image for display
    pil_image = Image.fromarray(rgb_image.to_memoryview().tobytes(), 'RGB')

    # Display the image
    st.image(pil_image, caption="Slide Image", use_column_width=True)




