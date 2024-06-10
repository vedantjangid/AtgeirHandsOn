def count_digits_and_alphabets(string):
    digit_count = 0
    alphabet_count = 0

    for char in string:
        if char.isdigit():
            digit_count += 1
        elif char.isalpha():
            alphabet_count += 1

    return digit_count, alphabet_count

# Prompt the user to enter a string
print("Enter a string: ", end="")
user_input = input()

# Count the number of digits and alphabets in the string
digit_count, alphabet_count = count_digits_and_alphabets(user_input)

# Print the results
print(f"Number of digits: {digit_count}")
print(f"Number of alphabets: {alphabet_count}")
