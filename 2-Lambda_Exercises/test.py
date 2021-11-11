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

print(count_partitions(15,15))