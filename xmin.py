def convert_coordinates(xmin, ymin, width, height):
    xmax = xmin + width
    ymax = ymin + height
    return xmin, ymin, xmax, ymax

x = 994
y = 550
w = 121
h = 28

xmin, ymin, xmax, ymax = convert_coordinates(x, y, w, h)
print(f'xmin: {xmin}, ymin: {ymin}, xmax: {xmax}, ymax: {ymax}')
