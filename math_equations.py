from math import sqrt

def distance(device_1, device_2):
    x_1, y_1 = device_1.location()
    x_2, y_2 = device_2.location()
    return sqrt((x_1-x_2)**2 + (y_1-y_2)**2)
