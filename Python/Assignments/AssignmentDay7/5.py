import numpy as np

zeros = np.zeros(10)

vowels = np.array(['a', 'e', 'i', 'o', 'u'])

ones = np.ones((2, 5), dtype=int)

myarray1 = np.array([[2.7, -2, -19], [0, 3.4, 99.9], [10.6, 0, 13]])

myarray2 = np.arange(4, 4 + 3*5*4, 4, dtype=float).reshape(3, 5)

print('')
print('Question A)')
print("zeros:\n", zeros)
print('')
print('Question B)')
print("\nvowels:\n", vowels)
print('')
print('Question C)')
print("\nones:\n", ones)
print('')
print('Question D)')
print("\nmyarray1:\n", myarray1)
print('')
print('Question E)')
print("\nmyarray2:\n", myarray2)
