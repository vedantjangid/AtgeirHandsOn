x = {'mango', 'apple'}
y = {'mango', 'orange'}
z = {'mango'}

def check_subsets(a, b):
    print(f"If {a} is subset of {b}")
    print(a <= b)  # Using comparison operator
    print(a.issubset(b))  # Using issubset() method
    print()



check_subsets(x, y)
check_subsets(y, x)
check_subsets(y, z)
check_subsets(z, y)
