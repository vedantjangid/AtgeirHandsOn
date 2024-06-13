D = {'a': 10, 'b': 37, 'c': 22, 'd': 33, 'e': 45, 'f': 9, 'g': 88, 'h': 63, 'i': 98, 'j': 12}

input1 = input("Input key 1: ")
input2 = input("Input key 2: ")
input3 = input("Input key 3: ")

value1 = D.get(input1)
value2 = D.get(input2)
value3 = D.get(input3)

if value1 is None or value2 is None or value3 is None:
    print("One or more keys are invalid.")
else:
    if value1 > value2 and value1 > value3:
        print(value1)
    elif value2 > value1 and value2 > value3:
        print(value2)
    else:
        print(value3)
