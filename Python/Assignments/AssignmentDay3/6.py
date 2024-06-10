def difference_from_17(num):
    diff = num - 17
    if num > 17:
        return abs(2 * diff)
    else:
        return abs(diff)

num = int(input("Enter number: "))

answer = difference_from_17(num)
print("Answer:", answer)
