def swap_with_third_var(a, b):
    temp = a
    a = b
    b = temp
    return a, b

def swap_without_third_var(a, b):
    a = a + b
    b = a - b
    a = a - b
    return a, b

# Prompt the user to enter two numbers
print("Enter the first number: ", end="")
num1 = float(input())
print("Enter the second number: ", end="")
num2 = float(input())

# Prompt the user to choose the method of swapping
print("Choose swapping method:")
print("1. With third variable")
print("2. Without third variable")
choice = int(input("Enter your choice: "))

# Perform swapping based on the user's choice
if choice == 1:
    num1, num2 = swap_with_third_var(num1, num2)
    print("Swapped numbers (with third variable):", num1, num2)
elif choice == 2:
    num1, num2 = swap_without_third_var(num1, num2)
    print("Swapped numbers (without third variable):", num1, num2)
else:
    print("Invalid choice. Please enter either 1 or 2.")
