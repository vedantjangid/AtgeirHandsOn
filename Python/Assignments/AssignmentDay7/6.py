import numpy as np

# Define the arrays as given
zeros = np.zeros(10)
vowels = np.array(['a', 'e', 'i', 'o', 'u'])
ones = np.ones((2, 5), dtype=int)
myarray1 = np.array([[2.7, -2, -19], [0, 3.4, 99.9], [10.6, 0, 13]])
myarray2 = np.arange(4, 4 + 3 * 5 * 4, 4, dtype=float).reshape(3, 5)

print('Question A)')
arrays = [zeros, vowels, ones, myarray1, myarray2]
for i, array in enumerate(arrays):
    print(f"Array {i + 1}: {array}")
    print("Dimensions:", array.ndim)
    print("Shape:", array.shape)
    print("Size:", array.size)
    print("Data type:", array.dtype)
    print("Item size:", array.itemsize, "bytes")
    print()

print('Question B)')
ones_reshaped = ones.reshape(1, 10)
print("Reshaped 'ones' array to a single row:\n", ones_reshaped)

print('Question C)')
print("2nd and 3rd element of 'vowels':", vowels[1:3])

print('Question D)')
print("All elements in the 2nd and 3rd row of 'myarray1':\n", myarray1[1:3])

print('Question E)')
print("Elements in the 1st and 2nd column of 'myarray1':\n", myarray1[:, :2])

print('Question F)')
print("Elements in the 1st column of the 2nd and 3rd row of 'myarray1':\n", myarray1[1:3, 0])

print('Question G)')
print("Reversed 'vowels' array:", vowels[::-1])
