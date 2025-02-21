'''1. Write a python program to reverse a number using a while loop. '''

# Input the number from the user
num = int(input("Enter a number: "))

# Initialize a variable to store the reversed number
reversed_num = 0

# Reverse the number using a while loop
while num > 0:
    # Extract the last digit of the number
    digit = num % 10
    # Add the digit to the reversed number
    reversed_num = reversed_num * 10 + digit
    # Remove the last digit from the number
    num = num // 10

# Print the reversed number
print(f"The reversed number is: {reversed_num}")

'''output:Enter a number: 76
The reversed number is: 67'''
