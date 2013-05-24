# merge function for second half of mergesort
def merge(left, right):
    merged_list = []
    left.reverse()
    right.reverse()
    while left and right:
        if left[-1] <= right[-1]:
            merged_list.append(left.pop())
        else:
            merged_list.append(right.pop())
    if left:
        merged_list.extend(left)
    else:
        merged_list.extend(right)
    return merged_list

# recursive part of mergesort
def mergesort(array):
    length = len(array)
    if length <= 1:
        return array
    mid = length // 2
    # this is black magic and stands in place of n assignments
    left = array[:mid]
    right = array[mid:]
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)



def quicksort(array):
    length = len(array)
    if length <= 1:
        return array
    p,i = pivot(array[0], array[length//2], length//2, array[-1])
    del array[i]
    less = []
    greater = []
    for x in array:
        if x <= p:
            less.append(x)
        else:
            greater.append(x)
    less = quicksort(less)
    less.append(p)
    less.extend(quicksort(greater))
    return less

# median-of-three pivot
def pivot(one, two, two_i, three):
    if one < two < three:
        return two, two_i
    elif two < one < three:
        return one, 0
    return three, -1


def heapsort():
    return
