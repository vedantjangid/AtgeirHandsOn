D1 = {'a': 10, 'b': 37, 'c': 22, 'd': 33}
D2 = {'e': 45, 'f': 9, 'g': 88, 'h': 63}

def addDict(x, y):
    z = y.copy() 
    z.update(x)   
    return z     

merged_dict = addDict(D1, D2)
print(merged_dict)
