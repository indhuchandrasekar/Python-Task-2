'''
Problem 7: To find first non repeating elememts in a given list of integers.
'''
# Define a function to find the first non-repeated element in a list
def first_non_repeated_el(lst):
    # Create a dictionary 'ctr' to count the occurrences of each element
    ctr = {}
    # Iterate through the elements in the list
    for i in lst:
        # If the element is already in the dictionary, increment its count
        if i in ctr:
            ctr[i] += 1
        # If the element is not in the dictionary, add it with a count of 1
        else:
            ctr[i] = 1
    # Iterate through the elements in the list again
    for i in lst:
        # Find the first element with a count of 1 (non-repeated)
        if ctr[i] == 1:
            return i
    # If no non-repeated element is found, return None

# Create a list of numbers
nums =  [1, 2, 3, 4, 5, 6, 7, 8, 1]

# Print the original list of numbers
print("Original list:")
print(nums)

# Call the first_non_repeated_el function with the list and store the result in 'result'
result = first_non_repeated_el(nums)

# Print the result, which is the first non-repeated element in the list
print("First non-repeated element in the said list:")
print(result)