input_string = input("Enter a string: ")

char_to_count = input("Enter the character to count: ")

if len(char_to_count) != 1:
    print("Please enter exactly one character.")
else:
    count = input_string.count(char_to_count)
    print(f"The character '{char_to_count}' occurs {count} times in the string.")
