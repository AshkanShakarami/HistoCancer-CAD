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

import streamlit as st
from openslide import open_slide

# Title
st.title("Whole Slide Image Viewer")

# File uploader widget
uploaded_file = st.file_uploader("Choose a .svs file...", type="svs")

# Check if an image is uploaded
if uploaded_file is not None:
    # Read the WSI
    slide = open_slide(uploaded_file)

    # Display slide information
    st.subheader("Slide Information:")
    st.write(f"- Level count: {slide.level_count}")
    st.write(f"- Dimensions: {slide.dimensions}")
    st.write(f"- Level dimensions: {slide.level_dimensions}")

    # Display an example image from the first level
    st.subheader("Example Image from Level 0:")
    level_0_image = slide.read_region((0, 0), 0, slide.level_dimensions[0])
    st.image(level_0_image, caption="Slide Image (Level 0)", use_column_width=True)

    # You can add more interactive features or analysis logic here


