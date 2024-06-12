class ComplexNumber:
    def __init__(self, real, imag):
        self.real = real
        self.imag = imag
    
    def getData(self):
        print(f"{self.real} + {self.imag}i")

    def __add__(self, other):
        return ComplexNumber(self.real + other.real, self.imag + other.imag)

# Creating objects c1 and c2
c1 = ComplexNumber(3, 4)
c2 = ComplexNumber(1, 2)

# Printing contents of c1 and c2
print("Contents of c1:")
c1.getData()
print("Contents of c2:")
c2.getData()

# Adding c1 and c2
result = c1 + c2

# Printing the addition
print("Result of addition:")
result.getData()
