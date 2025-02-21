'''1. Python program to check leap year  or not.'''

# Function to check if a year is a leap year
def is_leap_year(year):
    # Leap year is divisible by 4 but not divisible by 100, unless divisible by 400
    if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
        return True
    else:
        return False

# Input year from the user
year = int(input("Enter a year: "))

# Check if the year is a leap year
if is_leap_year(year):
    print(f"{year} is a Leap Year.")
else:
    print(f"{year} is not a Leap Year.")
    
'''output:Enter a year: 2025
2025 is not a Leap Year.'''
