'''1. Declare a div() function with two parameters. Then call the function and pass two numbers and display their division.'''

# Function to perform division
def div(num1, num2):
    # Check if the divisor is zero
    if num2 == 0:
        return "Error! Division by zero."
    else:
        return num1 / num2

# Call the function and pass two numbers
number1 = float(input("Enter the first number: "))
number2 = float(input("Enter the second number: "))

# Display the result of the division
result = div(number1, number2)
print(f"The result of division is: {result}")

'''Output:
Enter the first number: 2
Enter the second number: 3
The result of division is: 0.6666666666666666'''
