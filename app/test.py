import streamlit as st
import pandas as pd
import numpy as np


st.title("Paul Boudolf")
st.subheader("This is Paul's website")


image_path = "app/media/paul_LI.jpeg"
if st.button("Coucou"):
    st.image(image_path)