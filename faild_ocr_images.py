import pandas as pd
import os
import shutil

def copy_missing_images(image_folder, excel_path, output_folder):
    # Read the Excel sheet
    df = pd.read_csv(excel_path, header=None)
    
    # Filter rows where the second column is 'missing'
    missing_images = df[df.iloc[:, 6] == 'fail'].iloc[:, 0]
    print(missing_images)
    # Copy the missing images to the output folder
    for image_name in missing_images:
        image_path = os.path.join(image_folder, image_name)
        output_path = os.path.join(output_folder, image_name)
        shutil.copy(image_path, output_path)
        print(f"Copied {image_name} to {output_folder}.")

# Example usage
image_folder = "/home/vginne/ocr_pre_labelling/input"
excel_path = "/home/vginne/ocr_api_v5/api/github/api/api_test/bounding_boxes_from_andrea_ocr.csv"
output_folder = "/home/vginne/ocr_pre_labelling/fail_andrea_ocr"

copy_missing_images(image_folder, excel_path, output_folder)
print("done")
