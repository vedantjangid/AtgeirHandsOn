def remove_and_print_every_third(numbers):
    removed_numbers = []
    index = 0

    while len(numbers) > 0:
        index += 2  
        if index >= len(numbers):
            break
        removed_numbers.append(numbers.pop(index))
    
    return removed_numbers


numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14, 15]

removed_numbers = remove_and_print_every_third(numbers)
print("Removed every third consecutive number:", removed_numbers)
print("Remaining numbers in the list:", numbers)
