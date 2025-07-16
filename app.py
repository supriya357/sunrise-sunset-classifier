import streamlit as st
import joblib
import cv2
import numpy as np
from PIL import Image

# Load your trained model
model = joblib.load("sunrise_sunset_model.pkl")

# Settings
IMG_SIZE = 64
CLASS_NAMES = ["Sunrise", "Sunset"]

def predict_image(image: Image.Image):
    image_cv = cv2.cvtColor(np.array(image), cv2.COLOR_RGB2BGR)
    resized = cv2.resize(image_cv, (IMG_SIZE, IMG_SIZE))
    flattened = resized.flatten().reshape(1, -1)
    prediction = model.predict(flattened)
    return CLASS_NAMES[prediction[0]]

st.title("🌅 Sunrise or Sunset Classifier")
st.write("Upload one image to predict.")

uploaded = st.file_uploader("Upload Image", type=["jpg", "jpeg", "png"])
if uploaded:
    img = Image.open(uploaded)
    st.image(img, use_column_width=True)
    label = predict_image(img)
    st.success(f"Prediction: **{label}**")
