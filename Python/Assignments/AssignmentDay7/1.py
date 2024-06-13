import random
import string

def generate_random_string(length=10):
    """Generates a random alphabetical string of given length."""
    letters = string.ascii_letters  
    return ''.join(random.choice(letters) for _ in range(length))

def generate_random_value_between(min_val, max_val):
    """Generates a random integer between min_val and max_val (inclusive)."""
    return random.randint(min_val, max_val)

def generate_random_multiple_of_seven():
    """Generates a random multiple of 7 between 0 and 70 (inclusive)."""
    return random.choice(range(0, 71, 7))


random_string = generate_random_string(10)  
random_value = generate_random_value_between(5, 15)  
random_multiple_of_seven = generate_random_multiple_of_seven()

print(f"Random Alphabetical String: {random_string}")
print(f"Random Value Between 5 and 15: {random_value}")
print(f"Random Multiple of 7 Between 0 and 70: {random_multiple_of_seven}")
