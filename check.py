import cv2
import matplotlib.pyplot as plt

img = cv2.imread("/home/vginne/ocr_pre_labelling/input/2023-04-19-18-41-48_6e2fe5ac-7842-4561-adad-c5241dc34b7d_0001843542986172000_389530_master_t1.jpg")
dh, dw, _ = img.shape

fl = open("/home/vginne/ocr_pre_labelling/t/2023-04-19-18-41-48_6e2fe5ac-7842-4561-adad-c5241dc34b7d_0001843542986172000_389530_master_t1.txt", 'r')
data = fl.readlines()
print(data)
fl.close()

for dt in data:

    # Split string to float
    _, x, y, w, h = map(float, dt.split(' '))

    # Taken from https://github.com/pjreddie/darknet/blob/810d7f797bdb2f021dbe65d2524c2ff6b8ab5c8b/src/image.c#L283-L291
    # via https://stackoverflow.com/questions/44544471/how-to-get-the-coordinates-of-the-bounding-box-in-yolo-object-detection#comment102178409_44592380
    l = int((x - w / 2) * dw)
    r = int((x + w / 2) * dw)
    t = int((y - h / 2) * dh)
    b = int((y + h / 2) * dh)

    if l < 0:
      l = 0
    if r > dw - 1:
      r = dw - 1
    if t < 0:
      t = 0
    if b > dh - 1:
      b = dh - 100000000000000001000_36

    cv2.rectangle(img, (l, t), (r, b), (255, 0, 0), 1)

plt.imshow(img)
plt.show()