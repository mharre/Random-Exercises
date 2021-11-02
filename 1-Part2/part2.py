import random

def is_unique(l):
    if len(l) == len(set(l)):
        return True
    return False

# print(is_unique([1,5,5,7,9]))

# def all_possible_strings(l):
#     random.shuffle(l)
#     print(''.join(l))

# print(all_possible_strings(['a', 'e', 'i', 'o', 'u']))

def remove_nums(l):
    position = 3-1
    i = 0
    len_list = (len(l))
    while len_list > 0:
        i = (position+i) % len_list
        print(l.pop(i))
        len_list -= 1

# print(remove_nums([10,20,30,40,50,60,70,80,90]))