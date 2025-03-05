import streamlit as st

st.title("Тестовые изображения")
st.write(
    "Let's start building! For help and inspiration, head over"
    "to [docs.streamlit.io](https://docs.streamlit.io/)."
)

if "counter" not in st.session_state:
    st.session_state.counter = 0

st.session_state.counter += 1

st.session_state.counter

