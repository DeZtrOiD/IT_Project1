import streamlit as st
from ultralytics import YOLO
import numpy as np
from PIL import Image


@st.cache_data
def predict(path: str):
    image = np.array(Image.open(path).convert('RGB'))
    model = YOLO("yolo11n.pt")
    return model(image)[0].plot()


st.title("Тестовые изображения")

st.button('Удалить кэш', on_click=st.cache_data.clear())

st.header('Первый тест')
st.image('pages/images/im1.jpg', caption='Фото до обработки')
st.image(predict('pages/images/im1.jpg'), caption='Обработанное фото')

st.header('Второй тест')
st.image('pages/images/im2.jpg', caption='Фото до обработки')
st.image(predict('pages/images/im2.jpg'), caption='Обработанное фото')

st.header('Третий тест')
st.image('pages/images/im3.jpg', caption='Фото до обработки')
st.image(predict('pages/images/im3.jpg'), caption='Обработанное фото')

st.header('Четвертый тест')
st.image('pages/images/im4.jpg', caption='Фото до обработки')
st.image(predict('pages/images/im4.jpg'), caption='Обработанное фото')

st.header('Пятый тест')
st.image('pages/images/im5.jpg', caption='Фото до обработки')
st.image(predict('pages/images/im5.jpg'), caption='Обработанное фото')
