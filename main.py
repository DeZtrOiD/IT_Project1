import cv2
from ultralytics import YOLO
import streamlit as st
import numpy as np
import imageio.v3 as iio
from PIL import Image


@st.cache_resource
def predict(image):
    image = iio.imread(image)
    model = YOLO("yolo11n.pt")
    image = cv2.resize(image, (640, 640))
    image = np.array(image)
    return model(image)[0]


st.title('IT проекты')
st.write('Пиложение для детектирования объектов на фотографии.')

if 'counter' not in st.session_state:
    st.session_state.counter = 0
if 'user_photo' not in st.session_state:
    st.session_state.user_photo = None

st.session_state.counter += 1

st.session_state.counter

with st.form('Uploader'):
    st.header('Upload your photo')
    input_image = st.file_uploader('', ['png', 'jpg'])
    if input_image is not None:
        st.session_state.user_photo = input_image
    st.form_submit_button('Detect objects')
    if st.session_state.user_photo is not None:
        st.write(f'File uploaded: {st.session_state.user_photo.name}')

if st.session_state.user_photo is not None:
    st.image(st.session_state.user_photo, 'Uploded photo')
    # a = predict(st.session_state.user_photo)
    # st.image(a)
    image = np.array(Image.open(st.session_state.user_photo))
    model = YOLO("yolo11n.pt")
    results = model(image)
    annotated_image = results[0].plot()
    st.image(annotated_image, caption="Processed Image with Detections")

