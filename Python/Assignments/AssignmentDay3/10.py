def flatten_list(nested_list):
    flat_list = []
    for element in nested_list:
        if isinstance(element, list):
            flat_list.extend(flatten_list(element))
        else:
            flat_list.append(element)
    return flat_list

x = [[1, 2, 3], [10, [4, 6, 7]], 8]

flat_x = flatten_list(x)

# Print the result
print("Output:", flat_x)
