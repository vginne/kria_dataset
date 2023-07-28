import os
import xml.etree.ElementTree as ET

def extract_values_from_xml(xml_data):
    try:
        root = ET.fromstring(xml_data)
        plate_min_x = int(root.find('.//PlateMinX').text)
        plate_max_x = int(root.find('.//PlateMaxX').text)
        plate_min_y = int(root.find('.//PlateMinY').text)
        plate_max_y = int(root.find('.//PlateMaxY').text)
        return plate_min_x, plate_max_x, plate_min_y, plate_max_y
    except (ET.ParseError, AttributeError) as e:
        print(f"Error extracting values from XML: {e}")
        return None

def convert_to_yolo_format(image_width, image_height, plate_min_x, plate_max_x, plate_min_y, plate_max_y):
    image_center_x = image_width / 2
    image_center_y = image_height / 2
    box_width = plate_max_x - plate_min_x
    box_height = plate_max_y - plate_min_y
    box_center_x = plate_min_x + (box_width / 2)
    box_center_y = plate_min_y + (box_height / 2)
    normalized_center_x = box_center_x / image_width
    normalized_center_y = box_center_y / image_height
    normalized_width = box_width / image_width
    normalized_height = box_height / image_height
    return normalized_center_x, normalized_center_y, normalized_width, normalized_height

def process_images_in_folder(folder_path):
    for filename in os.listdir(folder_path):
        if filename.endswith('.jpg'):
            image_path = os.path.join(folder_path, filename)
            txt_filename = os.path.splitext(filename)[0] + '.txt'
            txt_filepath = os.path.join(folder_path, txt_filename)

            with open(image_path, 'rb') as file:
                data = file.read()

            start_marker = "<?xml"
            end_marker = "</View>"
            start_index = data.find(start_marker.encode())
            end_index = data.find(end_marker.encode(), start_index) + len(end_marker)
            xml_data = data[start_index:end_index].decode()

            values = extract_values_from_xml(xml_data)

            if values is not None:
                image_width, image_height = 4096, 2048  # Update with actual image dimensions
                yolo_values = convert_to_yolo_format(image_width, image_height, *values)

                with open(txt_filepath, 'w') as txt_file:
                    txt_file.write(f"0 {yolo_values[0]:.6f} {yolo_values[1]:.6f} {yolo_values[2]:.6f} {yolo_values[3]:.6f}\n")

                print(f"Processed {filename} and saved values to {txt_filename}")
            else:
                print(f"Error processing {filename}")

# Example usage
folder_path = '/home/vginne/project1/20211019_20211021'
process_images_in_folder(folder_path)



###  after ocr 4092*2052, before ocr 4095*2196  