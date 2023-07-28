import numpy as np
import cv2
import os


def image_resize(img):

  src = cv2.imread(img)
  for i in range(2):
    rows, cols, _channels = map(int, src.shape)
    ota = cv2.pyrDown(src, dstsize=(cols//2, rows//2))
    src = ota

  #subsampling

  rows, cols, _channels = map(int, src.shape)
  ota = cv2.resize(src, dsize= (cols//2, rows//2))
  return ota



directory = "/home/vginne/onsite/original"
folder_path = "/home/vginne/onsite/l3"


if not os.path.exists(folder_path):
    os.makedirs(folder_path)

for file in os.listdir(directory):
  img_path = os.path.join(directory, file)
  resized_image = image_resize(img_path)

  # Write the file in the folder

  file_path = os.path.join(folder_path, file)
  cv2.imwrite(file_path, resized_image)