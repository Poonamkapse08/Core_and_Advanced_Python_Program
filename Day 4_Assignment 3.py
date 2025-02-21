'''3. Python Program to Check if a Number is Positive, Negative or zero'''



# Function to check if the number is positive, negative, or zero
def check_number(number):
    if number > 0:
        return "Positive"
    elif number < 0:
        return "Negative"
    else:
        return "Zero"

# Input a number from the user
num = float(input("Enter a number: "))

# Check and print whether the number is positive, negative, or zero
result = check_number(num)
print(f"The number {num} is {result}.")

'''Output: Enter a number: 45
The number 45.0 is Positive
