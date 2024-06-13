vowels = ['a','e','i','o','u']

def char_count(str):

    total_vowels = 0
    total_consonants = 0

    for c in str:
        if c.isalpha():
            if c in vowels:
                 total_vowels += 1
            else:
                total_consonants += 1
    
    print(f"Total vowels: {total_vowels}")
    print(f"Total consonants: {total_consonants}")

char_count(input("Enter a string to count: "))