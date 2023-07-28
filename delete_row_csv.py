import csv

def delete_rows_with_word(csv_file, word):
    # Read the CSV file and filter rows containing the word
    with open(csv_file, 'r') as file:
        reader = csv.reader(file)
        rows = [row for row in reader if word not in row]

    # Write the filtered rows to a new CSV file
    with open(csv_file, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(rows)

    print("Rows containing '{}' were deleted and the CSV file was saved.".format(word))

# Provide the path to your CSV file and the word to search for
csv_file_path = '/home/vginne/ocr_api_v5/api/github/api/api_test/bounding_boxes_from_andrea_ocr.csv'
word_to_search = 'fail'

delete_rows_with_word(csv_file_path, word_to_search)
