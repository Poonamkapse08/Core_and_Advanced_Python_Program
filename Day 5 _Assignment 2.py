'''2. Declare a square() function with one parameter.Then call the function and pass one number and display the square of that number'''

# Function to calculate the square of a number
def square(num):
    return num ** 2

# Call the function and pass a number
number = float(input("Enter a number: "))

# Display the square of the number
result = square(number)
print(f"The square of {number} is: {result}")


'''Output:
Enter a number: 90
The square of 90.0 is: 8100.0'''
