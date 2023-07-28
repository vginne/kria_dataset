from PIL import Image
import os
from tqdm import tqdm
###  after ocr 4092*2052, before ocr 4095*2196  
# Specify the folder path containing the images
folder_path = "/home/vginne/detection/raw_data/input"

# Specify the target size for cropping
target_width = 4096
target_height = 2048

# Iterate over each file in the folder
for filename in tqdm(os.listdir(folder_path)):
    file_path = os.path.join(folder_path, filename)
    
    # Open the image
    image = Image.open(file_path)
    
    # Crop the image to the desired size
    cropped_image = image.crop((0, 0, target_width, target_height))
    
    # Save the cropped image with the same filename
    cropped_image.save(file_path)

    # Close the image
    image.close()
