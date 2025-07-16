import streamlit as st
import joblib
import numpy as np
import cv2
from PIL import Image

# Load model
model = joblib.load("sunrise_sunset_model.pkl")

# Image settings
IMG_SIZE = 64

def preprocess(image):
    image = image.resize((IMG_SIZE, IMG_SIZE))
    img_array = np.array(image).flatten().reshape(1, -1)
    return img_array

st.title("🌅 Sunrise vs Sunset Classifier")

uploaded_file = st.file_uploader("Upload an image", type=["jpg", "jpeg", "png"])

if uploaded_file is not None:
    image = Image.open(uploaded_file).convert('RGB')
    st.image(image, caption="Uploaded Image", use_column_width=True)

    processed = preprocess(image)
    prediction = model.predict(processed)[0]
    
    label = "🌄 Sunrise" if prediction == 0 else "🌇 Sunset"
    st.success(f"**Prediction:** {label}")

