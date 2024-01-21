# Problem 6: Python code to find dupicatesin the three lists
# initializing list of lists
test_list = [[2, 3, 5, 8], [2, 6, 7, 3], [10, 9, 2, 3]]
 
# printing original list
print("The original list is : " + str(test_list))
 
# common element extraction form N lists
# using list comprehension and set intersection
res = list(set(test_list[0]).intersection(*test_list[1:]))
 
# printing result
print("The common elements from N lists : " + str(res))