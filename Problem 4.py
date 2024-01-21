'''
Problem 4: Python Program to find the sum of the first and last digit of an interger.
'''
# We have a number
number = 124718
 
# We are type casting it in string
number = str(number)
 
# Storing first and last digit in a variable
# after type casting into Integer.
first_digit = int(number[0])
last_digit = int(number[-1])
 
# Adding these two variables
addition = first_digit + last_digit
 
# Display our output
print('Addition of first and last digit of the number is', 
      addition)