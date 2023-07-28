import os
import random
import shutil


# Path to the folders containing the images and annotations
image_folder = "/home/vginne/detection/no_plate/final_dataset/images"
annotation_folder = "/home/vginne/detection/no_plate/final_dataset/labels"

# Output directories for train, test, and valid sets
train_image_dir = "/home/vginne/project1/train/images"
train_annotation_dir = "/home/vginne/project1/train/labels"
test_image_dir = "/home/vginne/project1/test/images"
test_annotation_dir = "/home/vginne/project1/test/labels"
valid_image_dir = "/home/vginne/project1/valid/images"
valid_annotation_dir = "/home/vginne/project1/valid/labels"

# Create the output directories if they don't exist
os.makedirs(train_image_dir, exist_ok=True)
os.makedirs(train_annotation_dir, exist_ok=True)
os.makedirs(test_image_dir, exist_ok=True)
os.makedirs(test_annotation_dir, exist_ok=True)
os.makedirs(valid_image_dir, exist_ok=True)
os.makedirs(valid_annotation_dir, exist_ok=True)

# Get a list of image and annotation files
image_files = os.listdir(image_folder)
annotation_files = os.listdir(annotation_folder)

# Sort the file lists to ensure consistent order
image_files.sort()
annotation_files.sort()

# Set the random seed for reproducibility
random.seed(42)

# Shuffle the indices of the files
indices = list(range(len(image_files)))
random.shuffle(indices)

# Calculate the number of files for each set
train_size = int(0.8 * len(image_files))
test_size = int(0.1 * len(image_files))
valid_size = len(image_files) - train_size - test_size

# Split the files into train, test, and valid sets
train_indices = indices[:train_size]
test_indices = indices[train_size:train_size + test_size]
valid_indices = indices[train_size + test_size:]

# Move the files to their respective directories
for index in train_indices:
    image_file = image_files[index]
    annotation_file = annotation_files[index]
    shutil.copy(os.path.join(image_folder, image_file), train_image_dir)
    shutil.copy(os.path.join(annotation_folder, annotation_file), train_annotation_dir)

for index in test_indices:
    image_file = image_files[index]
    annotation_file = annotation_files[index]
    shutil.copy(os.path.join(image_folder, image_file), test_image_dir)
    shutil.copy(os.path.join(annotation_folder, annotation_file), test_annotation_dir)

for index in valid_indices:
    image_file = image_files[index]
    annotation_file = annotation_files[index]
    shutil.copy(os.path.join(image_folder, image_file), valid_image_dir)
    shutil.copy(os.path.join(annotation_folder, annotation_file), valid_annotation_dir)

print("done")
