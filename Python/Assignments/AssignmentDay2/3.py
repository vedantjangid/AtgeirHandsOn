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

print("Enter last number of a range: ", end="")
tillNumber=int(input())
# numbers = (1, 2, 30, 4, 5, 67, 7, 8, 9)
rnge = range(1,tillNumber+1 )


even_count = 0
odd_count = 0
prime_count = 0


for num in rnge:
    if num % 2 == 0:
        even_count += 1
    else:
        odd_count += 1
    
    if is_prime(num):
        prime_count += 1


print("Number of even numbers:", even_count)
print("Number of odd numbers:", odd_count)
print("Number of prime numbers:", prime_count)
