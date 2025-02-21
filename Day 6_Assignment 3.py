'''3. Write a python program finding the factorial of a given number using a while loop'''

# Input the number from the user
num = int(input("Enter a number: "))

# Initialize a variable to store the factorial result
factorial = 1

# Check if the number is non-negative
if num < 0:
    print("Factorial does not exist for negative numbers.")
else:
    # Find the factorial using a while loop
    while num > 1:
        factorial *= num
        num -= 1

    # Print the result
    print(f"The factorial is: {factorial}")

'''Output: Enter a number: 5
The factorial is: 120'''
