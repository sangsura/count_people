import streamlit as st
from PIL import Image
import api
from retinaface import RetinaFace
import numpy as np

st.header("Model classify people below:")
img = st.file_uploader('Upload a image: ')
if img is not None:
    img = Image.open(img).convert("RGB")
    img = np.array(img)
    resp=RetinaFace.detect_faces(img)
    resp=len(resp)
    st.write("Số người trong ảnh là:",resp)