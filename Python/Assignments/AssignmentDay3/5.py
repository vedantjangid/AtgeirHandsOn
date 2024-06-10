from datetime import date

def parse_date_input(date_str):
    return tuple(map(int, date_str.split(',')))

print("Enter start date in this format (yyyy,mm,dd): ", end='')
from_date_input = input()
print("Enter end date in this format (yyyy,mm,dd): ", end='')
to_date_input = input()

from_date_tuple = parse_date_input(from_date_input)
to_date_tuple = parse_date_input(to_date_input)

from_date = date(*from_date_tuple)
to_date = date(*to_date_tuple)

difference = to_date - from_date

# Print the result
print(f"Number of days between {from_date} and {to_date}: {difference.days} days")
