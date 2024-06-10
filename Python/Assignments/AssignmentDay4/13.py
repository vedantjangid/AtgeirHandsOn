def remove_greater_than(d, number):
    return {k: v for k, v in d.items() if v <= number}

D = {'a': 10, 'b': 37, 'c': 22, 'd': 33}
number = 30

result = remove_greater_than(D, number)
print(f"Entered number: {number}")
print(f"O/P: D = {result}")
