# Sample numbers
numbers = (1, 2, 3, 4, 5, 6, 7, 8, 9, 111)

# Initialize counters
count_even = 0
count_odd = 0

# Iterate through the numbers and count evens and odds
for number in numbers:
    if number % 2 == 0:
        count_even += 1
    else:
        count_odd += 1

# Output the results
print(f"Number of even numbers: {count_even}")
print(f"Number of odd numbers: {count_odd}")
