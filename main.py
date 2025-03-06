from ultralytics import YOLO
import streamlit as st
import numpy as np
from PIL import Image
from io import BytesIO


@st.cache_resource
def predict(image):
    image = np.array(Image.open(image).convert('RGB'))
    model = YOLO('yolo11n.pt')
    return model(image)[0].plot()


def convertToBytes(image):
    image = Image.fromarray(image.astype('uint8'), 'RGB')
    buf = BytesIO()
    image.save(buf, format='JPEG')
    return buf.getvalue()


st.title('IT проект 1 курс')
st.write('Приложение для детектирования объектов на фотографии.')

if 'user_photo' not in st.session_state:
    st.session_state.user_photo = None

with st.form('Uploader'):
    st.header('Загрузите своё фото')
    input_image = st.file_uploader('', ['png', 'jpg'])

    if input_image is not None:
        st.session_state.user_photo = input_image
    st.form_submit_button('Найти объекты')

    if st.session_state.user_photo is not None:
        st.write(f'Загружен файл: {st.session_state.user_photo.name}')


if st.session_state.user_photo is not None:
    st.image(st.session_state.user_photo, 'Загруженное фото')

    annotated_image = predict(st.session_state.user_photo)
    st.image(annotated_image, caption='Обработанное фото')

    byte_im = convertToBytes(annotated_image)
    st.download_button('Скачать изображение', data=byte_im,
                       file_name=f'_{st.session_state.user_photo.name}')
