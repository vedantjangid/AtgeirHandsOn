def inRange(number, start, end):
    rnge = range(start, end+1)
    if (number in rnge):
        print("Its in the range")
    else:
        print("Not in range")

start = int(input("Enter the start of range: "))
end = int(input("Enter the end of range: "))
number = int(input("Enter the number to check: "))

inRange(number, start, end)