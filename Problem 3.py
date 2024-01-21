'''
Problem 3: Find out how many numbers are there in the given python list [10,501,22,37,100,999,87,351] are happy numbers?
'''

def ss(n):
    r = 0
    while n > 0:
        d = n % 10
        r += d * d
        n //= 10
    return r
def is_happy(n):
    if n > 0:
        while True:
            if (n := ss(n)) == 1:
                return True
            if n == 4:
                break
    return False
a = [10,501,22,37,100,999,87,351]
for n in a:
    print(n, is_happy(n))