import math
import time
import resource

print("Enter a number: ", end="")
number = int(input())
counter = 0

def is_prime(n):
    if n <= 1:
        return False
    if n <= 3:
        return True
    if n % 2 == 0 or n % 3 == 0:
        return False
    
    i = 5
    while i * i <= n:
        if n % i == 0 or n % (i + 2) == 0:
            return False
        i += 6
    return True


start_time = time.time()


with open("prime_numbers_output.txt", "w") as file:

    for num in range(1, number + 1):
        if is_prime(num):
            counter+=1
            result = f"{num} is a prime number.\n"
            file.write(result)
       
        

end_time = time.time()


total_time = end_time - start_time


usage = resource.getrusage(resource.RUSAGE_SELF)
memory_usage = usage.ru_maxrss 


print(f"\nTotal prime numbers = {counter}")
print(f"Total time taken: {total_time:.6f} seconds")
print(f"Total memory used: {memory_usage} KB")
