import numpy as np

# Define the matrices
matrix1 = np.array([[1, 2, 3],
                    [4, 5, 6],
                    [7, 8, 9]])

matrix2 = np.array([[10, 11, 12],
                    [13, 14, 15],
                    [16, 17, 18]])

# Check if matrices are compatible for multiplication
if matrix1.shape[1] != matrix2.shape[0]:
    print("Multiplication is not possible. Number of columns in the first matrix must be equal to the number of rows in the second matrix.")
else:
    # Perform matrix multiplication
    result = np.dot(matrix1, matrix2)

    # Print the result matrix
    print("Result Matrix:")
    print(result)