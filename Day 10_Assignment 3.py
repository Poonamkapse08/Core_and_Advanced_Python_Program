'''3. Write a Python program to find duplicate values from a list and display those.'''

# Given list of numbers
numbers = [10, 20, 30, 40, 20, 10, 50, 30]

# Initialize an empty list to store duplicates
duplicates = []

# Iterate through the list and find duplicates
for num in numbers:
    # Check if the number appears more than once in the list and not already in the duplicates list
    if numbers.count(num) > 1 and num not in duplicates:
        duplicates.append(num)

# Output the duplicates
print(f"The duplicate values in the list are: {duplicates}")

'''Output: The duplicate values in the list are: [10, 20, 30]'''
