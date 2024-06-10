def to_uppercase(string):
    uppercase_string = ""
    for char in string:
        # Check if the character is lowercase
        if 'a' <= char <= 'z':
            # Convert lowercase character to uppercase
            uppercase_string += chr(ord(char) - 32)
        else:
            uppercase_string += char
    return uppercase_string

def to_lowercase(string):
    lowercase_string = ""
    for char in string:
        # Check if the character is uppercase
        if 'A' <= char <= 'Z':
            # Convert uppercase character to lowercase
            lowercase_string += chr(ord(char) + 32)
        else:
            lowercase_string += char
    return lowercase_string

# Prompt the user to enter a string
print("Enter a string: ", end="")
user_input = input()

# Convert the string to uppercase and lowercase
uppercase_result = to_uppercase(user_input)
lowercase_result = to_lowercase(user_input)

# Print the results
print("Uppercase:", uppercase_result)
print("Lowercase:", lowercase_result)
