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
from PIL import Image
import io
import os

# Title
st.title("HistoCancer-CAD: Whole Slide Image Viewer")

# File uploader widget
uploaded_file = st.file_uploader("Choose a .svs file...", type="svs")

# Check if an image is uploaded
if uploaded_file is not None:
    # Save the uploaded file locally
    with open("temp.svs", "wb") as f:
        f.write(uploaded_file.getvalue())

    # Open the slide image using PIL
    slide_image = Image.open("temp.svs")

    # Display the image using Streamlit
    st.image(slide_image, caption="Whole Slide Image", use_column_width=True)

    # Add more interactive features or analysis logic here

    # Remove the temporary file after the image is displayed
    os.remove("temp.svs")'''

import streamlit as st
from PIL import Image
import io
import os
import openslide
import subprocess

# Title
st.title("HistoCancer-CAD: Whole Slide Image Viewer")

# File uploader widget
uploaded_file = st.file_uploader("Choose a .svs file...", type="svs")

# Check if an image is uploaded
if uploaded_file is not None:
    # Save the uploaded file locally
    with open("temp.svs", "wb") as f:
        f.write(uploaded_file.getvalue())

    # Open the slide image using OpenSlide
    slide = openslide.OpenSlide("temp.svs")

    # Generate a Deep Zoom Image (DZI) pyramid
    dzi_file = "temp.dzi"
    subprocess.run(["openslide-deepzoom", "deepzoom", "convert", "temp.svs", dzi_file])

    # Display the DZI pyramid using OpenSeadragon
    st.write('<iframe src="viewer.html" width="100%" height="800px"></iframe>', unsafe_allow_html=True)

    # Remove the temporary files
    os.remove("temp.svs")
    os.remove(dzi_file)




















