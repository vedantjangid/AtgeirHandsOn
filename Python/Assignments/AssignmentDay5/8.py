def check_speed(speed):
    if speed < 70:
        print("Ok")
    else:
        demerit_points = (speed - 70) // 5
        if demerit_points > 12:
            print("License suspended")
        else:
            print(f"Points: {demerit_points}")


check_speed(65)  
check_speed(75)  
check_speed(85)  
check_speed(95)  
check_speed(130) 