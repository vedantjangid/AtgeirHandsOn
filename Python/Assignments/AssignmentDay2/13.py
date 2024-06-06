from num2words import num2words

def number_to_words(number):
    return num2words(number)

# Prompt the user to enter a number
print("Enter a number: ", end="")
user_input = int(input())

# Convert the number to words
result = number_to_words(user_input)

# Print the result
print(f"The number {user_input} in words is: {result.capitalize()}")
