import os
import shutil

def copy_txt_files(main_folder, destination_folder):
    # Create the destination folder if it doesn't exist
    if not os.path.exists(destination_folder):
        os.makedirs(destination_folder)

    # Iterate through all subdirectories and files in the main folder
    for root, dirs, files in os.walk(main_folder):
        for file in files:
            # Check if the file is a .txt file
            if file.endswith(".jpg"):
                # Get the full path of the source file
                source_file_path = os.path.join(root, file)
                # Construct the destination file path
                destination_file_path = os.path.join(destination_folder, file)
                # Copy the file to the destination folder
                shutil.copy(source_file_path, destination_file_path)
                print(f"Copied {source_file_path} to {destination_file_path}")

# Specify the main folder containing the subfolders with .txt files
main_folder = "/home/vginne/final_datasets/raw_data_no_plate_failed_by_ocr/transits_noPlate_4410134_03and04-2023/transits_noPlate/2023_04"

# Specify the destination folder where you want to copy the .txt files
destination_folder = "/home/vginne/to_hanusha"

# Call the function to copy the .txt files
copy_txt_files(main_folder, destination_folder)


