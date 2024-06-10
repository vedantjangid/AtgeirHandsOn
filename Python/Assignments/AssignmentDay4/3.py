d = {1: 10, 2: 20, 3: 30, 4: 40, 5: 50, 6: 60}

userInput = int(input("Enter a key to be checked: "))

result = d.get(userInput)

if (result != None): 
    print("Key is present in the dictionary")
else:
    print("Key is not present in the dictionary")
