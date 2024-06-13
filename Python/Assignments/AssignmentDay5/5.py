string = input("Enter a string to check if it's a palindrome: ")

def palindrome(str):
    orignal = str
    reversed_str = ''.join(reversed(orignal))  
    # print(f"Original string: {orignal}")
    # print(f"Reversed string: {reversed_str}")

    if orignal.lower() == reversed_str.lower():  
        print("The string is a palindrome")
    else:
        print("The string is not a palindrome")

palindrome(string)