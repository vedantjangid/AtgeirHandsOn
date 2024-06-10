def convert_distance(distance_km):
    """
    Convert the distance between two cities from kilometers to meters, feet, inches, and centimeters.
    
    Parameters:
        distance_km (float): The distance between two cities in kilometers.
        
    Returns:
        tuple: A tuple containing the converted distances in meters, feet, inches, and centimeters.
    """

    distance_m = distance_km * 1000
    

    distance_ft = distance_km * 3280.84
    

    distance_inches = distance_km * 39370.1
    

    distance_cm = distance_km * 100000
    
    return distance_m, distance_ft, distance_inches, distance_cm


distance_km = float(input("Enter the distance between two cities in kilometers: "))


distance_m, distance_ft, distance_inches, distance_cm = convert_distance(distance_km)


print("Distance in meters:", distance_m)
print("Distance in feet:", distance_ft)
print("Distance in inches:", distance_inches)
print("Distance in centimeters:", distance_cm)
