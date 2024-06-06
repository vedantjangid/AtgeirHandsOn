def is_palindrome(number):
    num_str = str(number)
    reversed_num_str = num_str[::-1]
    return num_str == reversed_num_str

print("Enter an integer: ", end="")
user_input = int(input())

if is_palindrome(user_input):
    print(f"The number {user_input} is a palindrome.")
else:
    print(f"The number {user_input} is not a palindrome.")
