import xml.etree.ElementTree as ET

def extract_xml_from_image(image_path):
    with open(image_path, 'rb') as file:
        data = file.read()

    start_marker = "<?xml"
    end_marker = "</View>"
    start_index = data.find(start_marker.encode())
    end_index = data.find(end_marker.encode(), start_index) + len(end_marker)

    xml_data = data[start_index:end_index].decode()

    # Parse the XML data
    root = ET.fromstring(xml_data)

    # Find the elements and extract the values
    plate_min_x = root.find('.//PlateMinX').text
    plate_max_x = root.find('.//PlateMaxX').text
    plate_min_y = root.find('.//PlateMinY').text
    plate_max_y = root.find('.//PlateMaxY').text

    # Print the extracted values
    print(f"PlateMinX: {plate_min_x}")
    print(f"PlateMaxX: {plate_max_x}")
    print(f"PlateMinY: {plate_min_y}")
    print(f"PlateMaxY: {plate_max_y}")

# Example usage
image_path = '/home/vginne/project1/test2.jpg'
extract_xml_from_image(image_path)

