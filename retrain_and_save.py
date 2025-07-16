import os
import cv2
import numpy as np
import joblib
from sklearn.model_selection import train_test_split
from sklearn.svm import SVC
from sklearn.pipeline import Pipeline
from sklearn.preprocessing import StandardScaler

# Constants
IMG_SIZE = 64
DATA_DIR = "train"  # your existing folders: train/sunrise & train/sunset

def load_data():
    X, y = [], []
    for label, folder in enumerate(["sunrise", "sunset"]):
        folder_path = os.path.join(DATA_DIR, folder)
        for filename in os.listdir(folder_path):
            img_path = os.path.join(folder_path, filename)
            img = cv2.imread(img_path)
            if img is not None:
                img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))
                X.append(img.flatten())
                y.append(label)
    return np.array(X), np.array(y)

# Load and split data
X, y = load_data()
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2)

# Create a safe pipeline
pipeline = Pipeline([
    ('scaler', StandardScaler()),
    ('svm', SVC())
])

pipeline.fit(X_train, y_train)

# Save model safely
joblib.dump(pipeline, "sunrise_sunset_model.pkl")

print("✅ Model trained and saved safely for Streamlit!")
