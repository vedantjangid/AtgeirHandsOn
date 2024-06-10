test_list = [(25, 6), (34, 7), (214, 235), (12, 45), (78,), (111, 22), [356, 729]]

filtered_list = [
    item for item in test_list 
    if isinstance(item, tuple) and any(100 <= x <= 999 for x in item)
]

print("Output:", filtered_list)
