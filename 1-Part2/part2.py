import random, pprint, collections

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

def three_sum(nums):
  result = []
  nums.sort()
  for i in range(len(nums)-2):
    if i > 0 and nums[i] == nums[i-1]:
      continue
    l, r = i+1, len(nums)-1
    while l < r:
      s = nums[i] + nums[l] + nums[r]
      if s > 0:
        r -= 1
      elif s < 0:
          l += 1
      else:
        # found three sum
        result.append((nums[i], nums[l], nums[r]))
        # remove duplicates
        while l < r and nums[l] == nums[l+1]:
          l+=1
          while l < r and nums[r] == nums[r-1]:
            r -= 1
            l += 1
            r -= 1
          return result

# x = [1, -6, 4, 2, -1, 2, 0, -2, 0 ]
# print(three_sum(x))

file_input = input('File Name: ')
with open(file_input, 'r') as info:
  count = collections.Counter(info.read().upper())
  value = pprint.pformat(count)
# print(value)