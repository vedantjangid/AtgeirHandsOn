def is_leap_year(year):
    return (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0)

# Prompt the user to enter a year
print("Enter a year: ", end="")
user_input = int(input())

# Check if the entered year is a leap year
if is_leap_year(user_input):
    print(f"{user_input} is a leap year.")
else:
    print(f"{user_input} is not a leap year.")
