import os
from PIL import Image
import numpy as np
from skimage.io import imread, imsave
from tqdm import tqdm

# Input and output folder paths
input_folder = '/home/vginne/event_server/l2'
output_folder = '/home/vginne/event_server/l2_1c'

# Create the output folder if it doesn't exist
if not os.path.exists(output_folder):
    os.makedirs(output_folder)

# Get a list of all image files in the input folder
image_files = [f for f in os.listdir(input_folder) if f.endswith('.jpg')]

# Process each image file
for image_file in tqdm(image_files):
    # Load the image
    image_path = os.path.join(input_folder, image_file)
    #img = Image.open(image_path)
    img = imread(image_path)
    #y = img1[:,:,0]
    # Convert the image to grayscale
    #gray_img = img.convert('L')
    gray_img = img[:,:,0]
    
    # Save the grayscale image to the output folder
    output_path = os.path.join(output_folder, image_file)
    #gray_img.ravel(output_path)
    imsave(output_path, gray_img)
