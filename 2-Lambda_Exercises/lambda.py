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

def binary_search(item_list,item):
	first = 0
	last = len(item_list)-1
	found = False
	while( first<=last and not found):
		mid = (first + last)//2
		if item_list[mid] == item:
			found = True
		else:
			if item < item_list[mid]:
				last = mid - 1
			else:
				first = mid + 1	
	return found

print(binary_search([1,2,3,5,8], 6))