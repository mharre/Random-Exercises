from functools import reduce

r = lambda x: x + 15
# print(r(10))
r = lambda x,y: x * y
# print(r(12,4))

def func_compute(n):
    return lambda x: x * n

# result = func_compute(2)
# print("Double the number of 15 =", result(15))

r = [('English', 88), ('Science', 90), ('Maths', 97), ('Social sciences', 82)]
r.sort(key=lambda tup: tup[1], reverse=True)
# print(r)

d = [{'make': 'Nokia', 'model': 216, 'color': 'Black'}, {'make': 'Mi Max', 'model': '2', 'color': 'Gold'}, {'make': 'Samsung', 'model': 7, 'color': 'Blue'}]
r = sorted(d, key=lambda d: d['color'])
# print(r)

d = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
r = filter(lambda x: x % 2 == 1,d)
# print(list(r))

def square(l):
    return list(map(lambda x: x ** 2, l))

# print(square(d))

# def starts_with(s, letter):
#     return set(map(lambda x: True if s.startswith(str(letter)) else False, s))

# print(starts_with('Python', 'P'))

starts_with = lambda x: True if x.startswith('P') else False
# print(starts_with('Python'))

fib_series = lambda n: reduce(lambda x, _: x+[x[-1]+x[-2]],
                                range(n-2), [0, 1])
                                
# print(fib_series(30))

is_num = lambda q: q.replace('.','',1).isdigit()
# print(is_num('26587'))
# print(is_num('4.2365'))
# print(is_num('-12547'))
# print(is_num('00'))
# print(is_num('A001'))
# print(is_num('001'))
# print("\nPrint checking numbers:")
is_num1 = lambda r: is_num(r[1:]) if r[0]=='-' else is_num(r)
# print(is_num1('-16.4'))
# print(is_num1('-24587.11'))

array_nums = [-1, 2, -3, 5, 7, 8, 9, -10]
# print("Original arrays:")
# print(array_nums)
result = sorted(array_nums, key = lambda i: 0 if i == 0 else -1 / i)
# print("\nRearrange positive and negative numbers of the said array:")
# print(result)

array_nums = [1, 2, 3, 5, 7, 8, 9, 10]
# print("Original arrays:")
# print(array_nums)
odd_ctr = len(list(filter(lambda x: (x%2 != 0) , array_nums)))
even_ctr = len(list(filter(lambda x: (x%2 == 0) , array_nums)))
# print("\nNumber of even numbers in the above array: ", even_ctr)
# print("\nNumber of odd numbers in the above array: ", odd_ctr)