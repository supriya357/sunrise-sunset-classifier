import os
import shutil
import random

# Paths
resized_dataset = "resized_dataset"
train_dir = "train"
val_dir = "val"

# Ensure directories exist
for category in ["sunrise", "sunset"]:
    os.makedirs(os.path.join(train_dir, category), exist_ok=True)
    os.makedirs(os.path.join(val_dir, category), exist_ok=True)

# Split function
def split_data(category):
    src_folder = os.path.join(resized_dataset, category)
    images = os.listdir(src_folder)
    random.shuffle(images)

    split_idx = int(0.8 * len(images))  # 80% for training, 20% for validation
    train_images = images[:split_idx]
    val_images = images[split_idx:]

    for img in train_images:
        shutil.move(os.path.join(src_folder, img), os.path.join(train_dir, category, img))

    for img in val_images:
        shutil.move(os.path.join(src_folder, img), os.path.join(val_dir, category, img))

# Run split for both categories
split_data("sunrise")
split_data("sunset")

print("✅ Dataset successfully split into train/ and val/")
