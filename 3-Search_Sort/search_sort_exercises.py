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

# print(binary_search([1,2,3,5,8], 6))

def sequential_search(l, val):
    pos = 0
    found = False

    while (pos <= len(l)-1 and not found):
        if l[pos] == val:
            found = True
        pos += 1

    return found, pos-1

# print(sequential_search([11,23,58,31,56,77,43,12,65,19], 19))


def ordered_binary_search(olist, item):
    
    if len(olist) == 0:
        return False
    else:
        midpoint = len(olist) // 2
        if olist[midpoint] == item:
            return True
        else:
            if item < olist[midpoint]:
                return binary_search(olist[:midpoint], item)
            else:
                return binary_search(olist[midpoint+1:], item)

# print(ordered_binary_search([0, 1, 3, 8, 14, 18, 19, 34, 52], 3))
# print(ordered_binary_search([0, 1, 3, 8, 14, 18, 19, 34, 52], 17))

def bubble_sort(l):
    for passnum in range(len(l)-1,0,-1):
        for i in range(passnum):
            if l[i] > l[i+1]:
                temp = l[i]
                l[i] = l[i+1]
                l[i+1] = temp

    return l

# print(bubble_sort([14,46,43,27,57,41,45,21,70]))
