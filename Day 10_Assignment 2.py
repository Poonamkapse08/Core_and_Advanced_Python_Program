'''2. Write a Python program to get the largest and smallest number from a list without built in functions.'''

# Given list of numbers
numbers = [10, 20, 4, 45, 99, 2]

# Initialize variables to store the largest and smallest numbers
largest = numbers[0]
smallest = numbers[0]

# Loop through the list to find the largest and smallest numbers
for num in numbers:
    if num > largest:
        largest = num
    if num < smallest:
        smallest = num

# Output the results
print(f"The largest number is: {largest}")
print(f"The smallest number is: {smallest}")

'''Output: The largest number is: 99
The smallest number is: 2'''


