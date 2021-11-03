from math import pi

def compute_area(r):
    r = float(r)
    result = pi * (r**2)
    return result

# print(compute_area(input('give radius of circle ')))

def reverse_name(str):
    return str[::-1]

# print(reverse_name(input('please enter first and last name: ')))

def list_tuple_gen(s):
    l = s.split(',')
    t = tuple(l)

    return f'List: {l}\nTuple: {t}'

# print(list_tuple_gen('3, 5, 7, 23'))


def difference(n):
    if n > 17:
        return abs(17-20) * 2

    if n < 17:
        return 17-n

# print(difference(20))

def num_within_range(n):
    if n in range(900,1001):
        return True
    if n in range(1900,2001):
        return True
    
    return f'You are {900-n} away from the first range\nand {1900-n} away from the second range'

# print(num_within_range(50))

def sum_three_times(x,y,z):
    if x in [y] and x in [z]:
        return (x+y+z) * 3

    return x+y+z

# print(sum_three_times(3,1,3))

def test(l):
    count = 0
    for num in l:
        if num == 4:
            count +=1

    return count

# print(test([1,2,4,5,4,4,3,4]))


def n_copies_of_first_two(s, n):
    if len(s) <= 2:
        return s * n
    s = s[:2] * n
    return s


# print(n_copies_of_first_two('p', 3))
# print(n_copies_of_first_two('abcd', 10))


