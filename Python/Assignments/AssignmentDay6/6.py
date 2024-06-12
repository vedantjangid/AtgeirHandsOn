class Rectangle:
    def __init__(self, length, width):
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

length = 5
width = 4
rectangle = Rectangle(length, width)

print("Length of the rectangle:", length)
print("Width of the rectangle:", width)
print("Area of the rectangle:", rectangle.area())
