import random

def get_user_list():
    user_input = input("Enter a list of items separated by commas: ")
    user_list = user_input.split(',')
    return user_list

user_list = get_user_list()

print("Orignal list:", user_list)
random.shuffle(user_list)
print("Shuffled list:", user_list)
