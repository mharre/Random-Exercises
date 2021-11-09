from functools import reduce
from collections import Counter

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

weekdays = ['Monday', 'Tuesday', 'Wednesday', 'Thursday', 'Friday', 'Saturday', 'Sunday']
days = filter(lambda day: day if len(day)==6 else '', weekdays)
for d in days:
  print(d)

nums1 = [1, 2, 3]
nums2 = [4, 5, 6]
# print("Original list:")
# print(nums1)
# print(nums2)
result = map(lambda x, y: x + y, nums1, nums2)
# print("\nResult: after adding two list")
# print(list(result))

students = []
sec_name = []
second_low = 0
n = int(input("Input number of students: "))
for _ in range(n):
   s_name = input("Name: ")
   score = float(input("Grade: "))
   students.append([s_name,score])
# print("\nNames and Grades of all students:")
# print(students)
order = sorted(students, key = lambda x: int(x[1]))
for i in range(n):
   if order[i][1] != order[0][1]:
       second_low = order[i][1]
       break
# print("\nSecond lowest grade: ",second_low)
sec_student_name = [x[0] for x in order if x[1] == second_low]
sec_student_name.sort()
# print("\nNames:")
for s_name in sec_student_name:
   print(s_name)

nums = [19, 65, 57, 39, 152, 639, 121, 44, 90, 190]
# print("Orginal list:")
# print(nums) 
result = list(filter(lambda x: (x % 19 == 0 or x % 13 == 0), nums)) 
# print("\nNumbers of the above list divisible by nineteen or thirteen:")
# print(result)


texts = ["php", "w3r", "Python", "abcd", "Java", "aaa"]
# print("Orginal list of strings:")
# print(texts) 
result = list(filter(lambda x: (x == "".join(reversed(x))), texts)) 
# print("\nList of palindromes:")
# print(result) 

texts = ["bcda", "abce", "cbda", "cbea", "adcb"]
# str = "abcd"
# print("Orginal list of strings:")
# print(texts) 
result = list(filter(lambda x: (Counter(str) == Counter(x)), texts)) 
# print("\nAnagrams of 'abcd' in the above string: ")
# print(result)

sample_names = ['sally', 'Dylan', 'rebecca', 'Diana', 'Joanne', 'keith']
sample_names=list(filter(lambda el:el[0].isupper() and el[1:].islower(),sample_names))
# print("Result:")
# print(len(''.join(sample_names)))

nums = [2, 4, -6, -9, 11, -12, 14, -5, 17]
# print("Original list:",nums)

total_negative_nums = list(filter(lambda nums:nums<0,nums))
total_positive_nums = list(filter(lambda nums:nums>0,nums))

# print("Sum of the positive numbers: ",sum(total_negative_nums))
# print("Sum of the negative numbers: ",sum(total_positive_nums))

def divisible_by_digits(start_num, end_num):
    return [n for n in range(start_num, end_num+1) \
                if not any(map(lambda x: int(x) == 0 or n%int(x) != 0, str(n)))]
# print(divisible_by_digits(1,22))

def rearrange_bigger(n):
    #Break the number into digits and store in a list
    nums = list(str(n))
    for i in range(len(nums)-2,-1,-1):
        if nums[i] < nums[i+1]:
            z = nums[i:]
            y = min(filter(lambda x: x > z[0], z))
            z.remove(y)
            z.sort()
            nums[i:] = [y] + z
            return int("".join(nums))
    return False
n = 12
# print("Original number:",n)
# print("Next bigger number:",rearrange_bigger(n))

n = 10
# print("\nOriginal number:",n)
# print("Next bigger number:",rearrange_bigger(n))
      
n = 201
# print("\nOriginal number:",n)
# print("Next bigger number:",rearrange_bigger(n))
n = 102
# print("\nOriginal number:",n)
# print("Next bigger number:",rearrange_bigger(n))
n = 445
# print("\nOriginal number:",n)
# print("Next bigger number:",rearrange_bigger(n))