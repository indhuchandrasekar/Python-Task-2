''''
Problem 1: Given a python list [10,501,22,37,100,999,87,351] Task is to create two list one is even numners and another is odd numbers.

'''
def Split(mix):
    ev_li = []
    od_li = []
    for i in mix:
        if (i % 2 == 0):
            ev_li.append(i)
        else:
            od_li.append(i)
    print("Even lists:", ev_li)
    print("Odd lists:", od_li)
 
 
# Driver Code
mix = [10,501,22,37,100,999,87,351]
Split(mix)