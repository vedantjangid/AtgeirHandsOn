import math


def calculate_distance(x1, y1, z1, x2, y2, z2):
    distance = math.sqrt((x2 - x1)**2 + (y2 - y1)**2 + (z2 - z1)**2)
    return distance


print("Enter the coordinates of the first point (x1, y1, z1):")
x1 = float(input("x1: "))
y1 = float(input("y1: "))
z1 = float(input("z1: "))


print("Enter the coordinates of the second point (x2, y2, z2):")
x2 = float(input("x2: "))
y2 = float(input("y2: "))
z2 = float(input("z2: "))


distance = calculate_distance(x1, y1, z1, x2, y2, z2)


print(f"The distance between the points ({x1}, {y1}, {z1}) and ({x2}, {y2}, {z2}) is {distance:.2f}")
