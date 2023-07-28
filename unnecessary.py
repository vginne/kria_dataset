import os


def delete_images_without_labels(image_folder, label_folder):
    # Get the list of files in the image folder
    image_files = os.listdir(image_folder)

    # Iterate over the image files
    for image_file in image_files:
        # Get the file name without extension
        image_name = os.path.splitext(image_file)[0]

        # Check if the corresponding label file exists
        label_file = os.path.join(label_folder, image_name + '.txt')
        if not os.path.exists(label_file):
            # Delete the image file
            image_path = os.path.join(image_folder, image_file)
            os.remove(image_path)
            print(f"Deleted image: {image_file}")

    print("Deletion complete!")

# Provide the paths to the image and label folders
image_folder = '/home/vginne/ocr_pre_labelling/to_hanusha_test'
label_folder = '/home/vginne/ocr_pre_labelling/t'

# Call the function to delete images without labels
delete_images_without_labels(image_folder, label_folder)
