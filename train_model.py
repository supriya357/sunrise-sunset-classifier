import os
import cv2
import numpy as np
import joblib

# Load the trained model
model = joblib.load("sunrise_sunset_model.pkl")

# Image parameters
IMG_SIZE = 64  # Same size used in training

# Function to preprocess an image
def preprocess_image(image_path):
    img = cv2.imread(image_path)
    img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))  # Resize to match training size
    img = img.flatten().reshape(1, -1)  # Flatten and reshape for prediction
    return img

# Test image path (replace with an actual image from validation set)
test_image_path = "val/sunset/example.jpg"  # Change to a real image path

if os.path.exists(test_image_path):
    test_image = preprocess_image(test_image_path)
    prediction = model.predict(test_image)
    
    category = "Sunrise" if prediction[0] == 0 else "Sunset"
    print(f"✅ Predicted: {category}")
else:
    print("❌ Error: Test image not found. Please check the file path.")
