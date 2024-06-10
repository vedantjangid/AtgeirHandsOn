# 8. Write a Python program to get unique values from a list.

print("Enter the list with duplicates: ", end='')
orignal_list = list(input().split(","))
print("Orignal list: ", orignal_list)
set_list = set(orignal_list)
print("Unique list: ", set_list)