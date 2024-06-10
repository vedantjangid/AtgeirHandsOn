input_string = input("Enter the values of the tuple separated by commas: ")

tple = tuple(map(int, input_string.split(' ')))

print(type(tple))

print("Original tuple:", tple)

revTuple = tple[::-1]
print("Reversed tuple:", revTuple)
