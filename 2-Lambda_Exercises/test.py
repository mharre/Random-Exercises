from math import sqrt

def summation(n, term):
    total, k = 0, 1
    while k <= n:
        total, k = total + term(k), k + 1
    return total

def identity(x):
    return x

def cube(x):
    return pow(x, 3)

def sum_naturals(n):
    return summation(n, identity)

def sum_cubes(n):
    return summation(n, cube)

# print(sum_naturals(5))

def sum_digits(n):
    if n < 10:
        return n
    else:
        all_but_last, last = n // 10, n % 10
        return sum_digits(all_but_last) + last

# print(sum_digits(18117))

def fact_iter(n):
    total, k = 1, 1
    while k <= n:
        total, k = total * k, k + 1
    return total

# print(fact_iter(4))

def fact(n):
    if n == 1:
        return 1
    else:
        return n * fact(n-1)

# print(fact(4))

def count_partitions(n, m):
        """Count the ways to partition n using parts up to m."""
        if n == 0:
            return 1
        elif n < 0:
            return 0
        elif m == 0:
            return 0
        else:
            return count_partitions(n-m, m) + count_partitions(n, m-1)

# print(count_partitions(15,15))

def count_up(n):
    """ prints numbers from 1 to n """
    if n == 1:
        print(n)
    else:
        count_up(n-1)
        print(n)
    
# count_up(5)

def cascade(n):
    if n < 10:
        print(n)
    else:
        print(n)
        print(cascade( n // 10))
        print(n)

# cascade(484)

def skip_add(n):
    if n <= 0:
        return 0
    else:
        return n + skip_add(n-2)

# print(skip_add(5))


def hailstone(n, steps=0):
    print(n)
    if n == 1:
        return steps+1
    elif n % 2 == 0:
        return hailstone(n//2, steps+1)
    else:
        return hailstone(n*3+1, steps+1)
    

# print(hailstone(10))

def summation(n, term):
    if n <= 0:
        return n
    else:
        return summation(n-1, term) + term(n)

# print(summation(5, lambda x: x * x * x))
# print(summation(9, lambda x: x + 1))
# print(summation(5, lambda x: 2**x))

def gcd(a,b):
    if a > b and a % b != 0:
        return gcd(b, a%b)
    else:
        return gcd(a, a%b)

print(gcd(34,19))
