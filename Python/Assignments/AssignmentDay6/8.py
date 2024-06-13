class CustomException(Exception):
    def __init__(self, message):
        super().__init__(message)

def check_positive_number(num):
    if num <= 0:
        raise CustomException("Number must be positive")

try:
    num = int(input("Enter a positive number: "))
    check_positive_number(num)
    print("You entered a positive number!")
except ValueError:
    print("Invalid input! Please enter a valid number.")
except CustomException as e:
    print("Custom Exception:", e)
