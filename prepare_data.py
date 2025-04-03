import os
import cv2

# Dataset paths
original_dataset = "dataset"
resized_dataset = "resized_dataset"  # New folder for resized images
IMG_SIZE = 224  # Resize all images to 224x224

# Ensure resized dataset directory exists
os.makedirs(resized_dataset, exist_ok=True)

# Function to resize images
def resize_and_save_images(category):
    input_folder = os.path.join(original_dataset, category)
    output_folder = os.path.join(resized_dataset, category)
    os.makedirs(output_folder, exist_ok=True)
    
    for img_name in os.listdir(input_folder):
        img_path = os.path.join(input_folder, img_name)
        img = cv2.imread(img_path)
        
        if img is not None:
            img = cv2.resize(img, (IMG_SIZE, IMG_SIZE))  # Resize to 224x224
            cv2.imwrite(os.path.join(output_folder, img_name), img)

# Resize images for both categories
resize_and_save_images("sunrise")
resize_and_save_images("sunset")

print("✅ Images resized and saved in 'resized_dataset/'")


