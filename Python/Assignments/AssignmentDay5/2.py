Sample_List = [8, 2, 3, 0, 7]

def sumOfAll(args):
    total = 0
    for i in args:
        total += i
    return total

total_sum = sumOfAll(Sample_List)
print(f"The sum of all elements in the list is {total_sum}")
