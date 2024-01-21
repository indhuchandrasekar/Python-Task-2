
'''
Problem 9 : Given Python list[10,20,30,9] and a value of 59.
write a python program to find the triplet in the list whose sum is equal to the given value
'''
from itertools import combinations
 
def findTriplets(lst, key):
     
    def valid(val):
        return sum(val) == key
         
    return list(filter(valid, list(combinations(lst, 3))))
 
# Driver Code
lst = [10, 20, 30, 9]
print(findTriplets(lst, 59))