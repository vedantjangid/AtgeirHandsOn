import math

print("Enter cylinder radius: ", end='')
radius = float(input())
print("Enter cylinder height: ", end='')
height = float(input())


surface_area = 2 * math.pi * radius * (radius + height)
floor_surface_area = math.floor(surface_area)


volume = math.pi * radius**2 * height
floor_volume = math.floor(volume)

print("Surface Area of the cylinder is: ", floor_surface_area)
print("Volume of the cylinder is: ", floor_volume)
