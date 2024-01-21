'''
Problem 10 : Given Python list[4,2,-3,1,6].
write a python program to find the sublist whose sum is equal to the zero
'''
from itertools import combinations
 
def sublist(lst, key):
     
    def valid(val):
        return sum(val) == key
         
    return list(filter(valid, list(combinations(lst, 3))))
 
# Driver Code
lst = [4,2,-3,1,6]
print(sublist(lst, 0))