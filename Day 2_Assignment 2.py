'''2. Declare two variables and print that which variable is largest using ternary operators'''

# Declare two variables
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))

# Using ternary operator to find the largest number
largest = num1 if num1 > num2 else num2

# Output the result
print(f"The largest number is: {largest}")

'''output:Enter the first number: 66
Enter the second number: 78
The largest number is: 78.0
