'''2. Write a Python program to remove duplicate characters of a given string.
Input = “String and String Function”'''

# Given input string
input_string = "String and String Function"

# Split the string into words
words = input_string.split()

# Initialize an empty string to store the result without duplicates
result = ""
seen = set()

# Loop through each word in the string
for word in words:
    # Add the word to the result only if it hasn't been added before
    if word.lower() not in seen:
        result += word + " "
        seen.add(word.lower())  # Mark this word as seen (case-insensitive)

# Output the result
print(f"{result.strip()}")


'''Ouput: String and Function'''
