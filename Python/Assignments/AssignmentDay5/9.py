def sum_multiples(limit):
    sum_of_multiples = 0
    for num in range(limit):
        if num % 3 == 0 or num % 5 == 0:
            sum_of_multiples += num
    return sum_of_multiples

def sum_common_multiples(limit):
    sum_of_common_multiples = 0
    for num in range(limit):
        if num % 3 == 0 and num % 5 == 0:
            sum_of_common_multiples += num
    return sum_of_common_multiples


limit = 30
print(f"Sum of multiples of 3 and 5 up to {limit}: {sum_multiples(limit)}")
print(f"Sum of common multiples of 3 and 5 up to {limit}: {sum_common_multiples(limit)}")