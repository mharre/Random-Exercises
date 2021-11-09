from random import randrange
import time

"""Lab 1: Expressions and Control Structures"""

def both_positive(x, y):
    if x and y >= 0:
        return True
    return False


def sum_digits(n):
    """Sum all the digits of n.

    >>> sum_digits(10) # 1 + 0 = 1
    1
    >>> sum_digits(4224) # 4 + 2 + 2 + 4 = 12
    12
    >>> sum_digits(1234567890)
    45
    >>> x = sum_digits(123) # make sure that you are using return rather than print
    >>> x
    6
    """
    s = 0
    while n:
        s += n % 10
        n //= 10
    return s

# print(both_positive(1,2))
# print(sum_digits(1234567890))

def hailstone(n):
    steps = 1
    while n > 1:
        if n % 2 == 0:
            n = n // 2
            steps += 1
        else:
            n = n*3+1
            steps += 1
    return steps
        

a = []
for num in range(1000):
    b = hailstone(randrange(10,10000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000000))
    if b not in a:
        a.append(b)

print(max(a))