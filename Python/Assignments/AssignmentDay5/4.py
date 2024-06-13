Sample_String = input("Enter a string: ")

def count_case(string):
    uppercase_count = 0
    lowercase_count = 0
    
    for char in string:
        if char.isupper():
            uppercase_count += 1
        elif char.islower():
            lowercase_count += 1
        else:
            continue
    
    print(f"Uppercase characters: {uppercase_count}")
    print(f"Lowercase characters: {lowercase_count}")

count_case(Sample_String)