import cmath

a = int(input("Enter a: "))
b = int(input("Enter b: "))
c = int(input("Enter c: "))

def roots(a, b, c):
    discriminant = b**2 - 4*a*c
    root1 = (-b + cmath.sqrt(discriminant)) / (2*a)
    root2 = (-b - cmath.sqrt(discriminant)) / (2*a)
    
    return root1, root2


root1, root2 = roots(a, b, c)
print(f"The roots of the equation {a}x^2 + {b}x + {c} are {root1} and {root2}")
