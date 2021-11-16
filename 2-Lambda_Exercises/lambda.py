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

def max_length_list(input_list):
    max_length = max(len(x) for x in input_list )   
    max_list = max(input_list, key = lambda i: len(i))    
    return(max_length, max_list)
    
def min_length_list(input_list):
    min_length = min(len(x) for x in input_list )  
    min_list = min(input_list, key = lambda i: len(i))
    return(min_length, min_list)
      
list1 = [[0], [1, 3], [5, 7], [9, 11], [13, 15, 17]]
# print("Original list:")
# print(list1)
# print("\nList with maximum length of lists:")
# print(max_length_list(list1))
# print("\nList with minimum length of lists:")
# print(min_length_list(list1))

def sort_sublists(input_list):
    result = [sorted(x, key = lambda x:x[0]) for x in input_list] 
    return result
color1 = [["green", "orange"], ["black", "white"], ["white", "black", "orange"]]
# print("\nOriginal list:")
# print(color1)  
# print("\nAfter sorting each sublist of the said list of lists:")
# print(sort_sublists(color1))

def sort_sublists(input_list):
    result = sorted(input_list, key=lambda l: (len(l), l))
    return result
list1 = [[2], [0], [1, 3], [0, 7], [9, 11], [13, 15, 17]]
# print("Original list:")
# print(list1)
# print("\nSort the list of lists by length and value:")
# print(sort_sublists(list1))

def max_val(list_val):
     max_val = max(list_val, key = lambda i: (isinstance(i, int), i))  
     return(max_val)

list_val = ['Python', 3, 2, 4, 5, 'version'] 
# print("Original list:")
# print(list_val)
# print("\nMaximum values in the said list using lambda:")
# print(max_val(list_val))

def sort_matrix(M):
    result = sorted(M, key=lambda matrix_row: sum(matrix_row)) 
    return result

matrix1 = [[1, 2, 3], [2, 4, 5], [1, 1, 1]]
matrix2 = [[1, 2, 3], [-2, 4, -5], [1, -1, 1]]

# print("Original Matrix:")
# print(matrix1)
# print("\nSort the said matrix in ascending order according to the sum of its rows") 
# print(sort_matrix(matrix1))
# print("\nOriginal Matrix:")
# print(matrix2) 
# print("\nSort the said matrix in ascending order according to the sum of its rows") 
# print(sort_matrix(matrix2))

def extract_string(str_list1, l):
    result = list(filter(lambda e: len(e) == l, str_list1))
    return result

str_list1 = ['Python', 'list', 'exercises', 'practice', 'solution'] 
# print("Original list:")
# print(str_list1)
l = 8
# print("\nlength of the string to extract:")
# print(l)
# print("\nAfter extracting strings of specified length from the said list:")
# print(extract_string(str_list1 , l))

def count_integer(list1):
    ert = list(map(lambda i: isinstance(i, float), list1)) 
    result = len([e for e in ert if e])         
    return result
list1 = [1, 'abcd', 3.12, 1.2, 4, 'xyz', 5, 'pqr', 7, -5, -12.22]
# print("Original list:")
# print(list1)
# print("\nNumber of floats in the said mixed list:")
# print(count_integer(list1))

def check_string(str1):
    messg = [
    lambda str1: any(x.isupper() for x in str1) or 'String must have 1 upper case character.',
    lambda str1: any(x.islower() for x in str1) or 'String must have 1 lower case character.',
    lambda str1: any(x.isdigit() for x in str1) or 'String must have 1 number.',
    lambda str1: len(str1) >= 7                 or 'String length should be atleast 8.',]
    result = [x for x in [i(str1) for i in messg] if x != True]
    if not result:
        result.append('Valid string.')
    return result    
s = input("Input the string: ")
# print(check_string(s))

def filter_data(students):
    result = dict(filter(lambda x: (x[1][0], x[1][1]) > (6.0, 70), students.items()))
    return result  
students = {'Cierra Vega': (6.2, 70), 'Alden Cantrell': (5.9, 65), 'Kierra Gentry': (6.0, 68), 'Pierre Cox': (5.8, 66)}
# print("Original Dictionary:")
# print(students)
# print("\nHeight> 6ft and Weight> 70kg:")
# print(filter_data(students))

def is_sort_list(nums, key=lambda x: x):
    for i, e in enumerate(nums[1:]):
        if key(e) < key(nums[i]): 
            return False
    return True
nums1 = [1,2,4,6,8,10,12,14,16,17]
# print ("Original list:")
# print(nums1)
# print("\nIs the said list is sorted!")
# print(is_sort_list(nums1)) 
nums2 = [2,3,8,4,7,9,8,2,6,5,1,6,1,2,3,4,6,9,1,2]
# print ("\nOriginal list:")
# print(nums1)
# print("\nIs the said list is sorted!")
# print(is_sort_list(nums2))

def index_on_inner_list(list_data, index_no):
    result = sorted(list_data, key=lambda x: x[index_no])
    return result
students = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] 
# print ("Original list:")
# print(students)
# index_no = 0
# print("\nSort the said list of lists by a given index","( Index = ",index_no,") of the inner list")
# print(index_on_inner_list(students, index_no))
# index_no = 2
# print("\nSort the said list of lists by a given index","( Index = ",index_no,") of the inner list")
# print(index_on_inner_list(students, index_no))

def index_on_inner_list(list1, list2):
    result = list(filter(lambda x: x not in list2, list1))
    return result
list1 = [1,2,3,4,5,6,7,8,9,10]
list2 = [2,4,6,8]
# print("Original lists:")
# print("list1:", list1)
# print("list2:", list2)
# print("\nRemove all elements from 'list1' present in 'list2:")
# print(index_on_inner_list(list1, list2))

def find_substring(str1, sub_str):
    result = list(filter(lambda x: sub_str in x, str1))
    return result
colors = ["red", "black", "white", "green", "orange"]
# print("Original list:")
# print(colors)

# sub_str = "ack"
# print("\nSubstring to search:")
# print(sub_str)
# print("Elements of the said list that contain specific substring:")
# print(find_substring(colors, sub_str))
# sub_str = "abc"
# print("\nSubstring to search:")
# print(sub_str)
# print("Elements of the said list that contain specific substring:")
# print(find_substring(colors, sub_str))

def intersection_nested_lists(l1, l2):
    result = [list(filter(lambda x: x in l1, sublist)) for sublist in l2]
    return result
nums1 = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13, 14]
nums2 = [[12, 18, 23, 25, 45], [7, 11, 19, 24, 28], [1, 5, 8, 18, 15, 16]]
# print("\nOriginal lists:")
# print(nums1)
# print(nums2)
# print("\nIntersection of said nested lists:")
# print(intersection_nested_lists(nums1, nums2))

def extract_nth_element(test_list, n):
    result = list(map (lambda x:(x[n]), test_list))
    return result
students = [('Greyson Fulton', 98, 99), ('Brady Kent', 97, 96), ('Wyatt Knott', 91, 94), ('Beau Turnbull', 94, 98)] 
# print ("Original list:")
# print(students)
# n = 0
# print("\nExtract nth element ( n =",n,") from the said list of tuples:")
# print(extract_nth_element(students, n))
# n = 2
# print("\nExtract nth element ( n =",n,") from the said list of tuples:")
# print(extract_nth_element(students, n))
