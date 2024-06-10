datalist = [1452, 11.23, 1+2j, True, 'Atgeir', (0, -1), [5, 12], {"class":'V', "section":'A'}]

def get_type(elem):
    return type(elem)


types_of_elements = map(get_type, datalist)

types_of_elements = list(types_of_elements)

print(types_of_elements)