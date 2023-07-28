
import os

def convert_to_yolo_format(csv_file, output_path, image_width, image_height):
    with open(csv_file, 'r') as file:
        lines = file.readlines()

    data = {}
    for line in lines:
        values = line.strip().split(',')

        if len(values) != 7:
            print(f"Ignoring invalid line: {line}")
            continue

        image_name = values[0]
        try:
            min_x = int(values[1])
            max_x = int(values[2])
            min_y = int(values[3])
            max_y = int(values[4])
        except ValueError:
            print(f"Ignoring invalid line: {line}")
            continue

        if image_name not in data:
            data[image_name] = []

        bbox_width = max_x - min_x
        bbox_height = max_y - min_y

        normalized_x = (min_x + bbox_width / 2) / image_width
        normalized_y = (min_y + bbox_height / 2) / image_height
        normalized_width = bbox_width / image_width
        normalized_height = bbox_height / image_height

        data[image_name].append((normalized_x, normalized_y, normalized_width, normalized_height))

    for image_name, bbox_list in data.items():
        txt_file = os.path.join(output_path, image_name.replace('.jpg', '.txt'))
        with open(txt_file, 'w') as file:
            for bbox in bbox_list:
                file.write(f"0 {bbox[0]} {bbox[1]} {bbox[2]} {bbox[3]}\n")

        print(f"Generated {txt_file} for image {image_name}")

# Provide the path to your CSV file
csv_file = '/home/vginne/ocr_api_v5/api/github/api/api_test/bounding_boxes_from_andrea_ocr.csv'

# Set the image width and height (you need to provide these values)
image_width = 4096
image_height = 2048

# Provide the path where the generated text files should be saved
output_path = '/home/vginne/ocr_pre_labelling/t'

convert_to_yolo_format(csv_file, output_path, image_width, image_height)
