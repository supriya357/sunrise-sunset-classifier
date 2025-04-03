import os
import joblib
import cv2
import numpy as np

# Load the trained model
model = joblib.load("sunrise_sunset_model.pkl")

# Image size (must match training size)
IMG_SIZE = 64  # Change from 224 to 64

# Function to preprocess and predict an image
def predict_image(image_path):
    image = cv2.imread(image_path)
    if image is None:
        print(f"❌ Error: Could not read {image_path}")
        return
    image = cv2.resize(image, (IMG_SIZE, IMG_SIZE))  # Resize to 64x64
    image = image.flatten().reshape(1, -1)  # Flatten and reshape
    prediction = model.predict(image)  # Predict
    label = "Sunrise" if prediction[0] == 0 else "Sunset"
    print(f"✅ Prediction: {label} for {image_path}")

# Test images
test_images = ["test_images/image.1.jpg", "test_images/image.2.jpg"]

for img_path in test_images:
    if os.path.exists(img_path):
        predict_image(img_path)
    else:
        print(f"⚠️ Warning: {img_path} not found. Add test images!")
