import os
import shutil
from pathlib import Path

def find_and_copy_similar_images(folder1, folder2, output_folder):
    # Get lists of files in the input folders
    folder1_files = set(os.listdir(folder1))
    folder2_files = set(os.listdir(folder2))

    # Find the intersection of file names to get similar images
    similar_files = folder1_files.intersection(folder2_files)

    # Create the output folder if it doesn't exist
    Path(output_folder).mkdir(parents=True, exist_ok=True)

    # Copy the similar images to the output folder
    for filename in similar_files:
        src_path = os.path.join(folder1, filename)
        dst_path = os.path.join(output_folder, filename)
        shutil.copy(src_path, dst_path)
        print(f"Copying {filename} to {output_folder}")

if __name__ == "__main__":
    folder1 = "/home/vginne/ocr_pre_labelling/deteced_by_kria_ocr"
    folder2 = "/home/vginne/ocr_pre_labelling/detected_by_andrea_ocr"
    output_folder = "/home/vginne/ocr_pre_labelling/detected_by_both_ocr"

    find_and_copy_similar_images(folder1, folder2, output_folder)
