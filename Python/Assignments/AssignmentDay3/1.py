#Sample data : [1, 3, 5, 7, 9, 10], [2, 4, 6, 8]
#Expected Output: [1, 3, 5, 7, 9, 2, 4, 6, 8]

orignal=[1, 3, 5, 7, 9, 10]
toInser=[2, 4, 6, 8]

orignal.pop()
orignal.extend(toInser)

print(orignal)