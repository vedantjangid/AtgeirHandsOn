def add_values(a, b):
    try:
        result = a + b
    except TypeError:
        if isinstance(a, (int, float, complex)):
            a = str(a)
        if isinstance(b, (int, float, complex)):
            b = str(b)
        result = a + b
    return result

a = 3
b = 'Data'
print("a + b =", add_values(a, b))

x = True
y = 10
print("x + y =", add_values(x, y))

p = 2.5
q = 7.5
print("p + q =", add_values(p, q))

