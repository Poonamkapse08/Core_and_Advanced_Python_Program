'''2. Python Program to Find the Largest Among Three Numbers'''

# Function to find the largest among three numbers
def find_largest(num1, num2, num3):
    # Check if num1 is greater than both num2 and num3
    if num1 >= num2 and num1 >= num3:
        return num1
    # Check if num2 is greater than both num1 and num3
    elif num2 >= num1 and num2 >= num3:
        return num2
    # Otherwise, num3 must be the largest
    else:
        return num3

# Input three numbers from the user
num1 = float(input("Enter the first number: "))
num2 = float(input("Enter the second number: "))
num3 = float(input("Enter the third number: "))

# Find and display the largest number
largest = find_largest(num1, num2, num3)
print(f"The largest number is: {largest}")

'''output:Enter the first number: 56
Enter the second number: 78
Enter the third number: 4
The largest number is: 78.0

