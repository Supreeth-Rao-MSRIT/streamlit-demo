import streamlit as st
from PIL import Image

from img_classification import machine_classification

st.title("Machines See Differently")
st.header("Cats vs Dogs")
st.text("Upload your image")

uploaded_file = st.file_uploader("Choose an image", type="jpg")
if uploaded_file is not None:
    image = Image.open(uploaded_file)
    st.image(image, caption='Uploaded image.', use_column_width=True)
    st.write("")
    st.write("Classifying...")
    label = machine_classification(image, 'Dogs-vs-Cats_model.h5')
    if label == 0:
        st.write("Dog")
    else:
        st.write("Cat")
