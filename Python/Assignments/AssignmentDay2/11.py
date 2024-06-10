def rearrange_number(number):
    num_str = str(number)
    length = len(num_str)
    rearranged = []

    for i in range((length + 1) // 2):
        rearranged.append(num_str[i]) 
        if i != length - i - 1:  
            rearranged.append(num_str[length - i - 1])  

    return ''.join(rearranged)

numbers = [12345, 90213, 123456]

for number in numbers:
    print(rearrange_number(number))
