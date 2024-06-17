import math

def calculate_circle_area(radius):
    """
    Calculate the area of a circle given its radius.
    
    Parameters:
        radius (float): The radius of the circle.
        
    Returns:
        float: The area of the circle.
    """
    area = math.pi * radius ** 2
    return area

# Input radius from the user
radius = float(input("Enter the radius of the circle: "))

# Calculate the area of the circle
area = calculate_circle_area(radius)

# Print the result
print("The area of the circle with radius", radius, "is:", area)
