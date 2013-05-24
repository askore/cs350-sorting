# merge function for second half of mergesort
def merge(left, right):
    merged_list = []
    l_len = len(left)
    r_len = len(right)
    while (l_len > 0 and r_len > 0):
        if left[0] <= right[0]:
            merged_list.append(left[0])
            left = left[1:]
            l_len = l_len - 1
        else:
            merged_list.append(right[0])
            right = right[1:]
            r_len = r_len - 1
    if l_len > 0:
        merged_list.extend(left)
    else:
        merged_list.extend(right)
    return merged_list

# recursive part of mergesort
def mergesort(array):
    length = len(array)
    if length <= 1:
        return array
    mid = int(length / 2)
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
    p,i = pivot(array[0], array[int(length/2)], int(length/2), array[-1])
    array.remove(p)
    less = []
    greater = []
    for x in array:
        if x <= p:
            less.append(x)
        else:
            greater.append(x)
    temp = []
    temp = quicksort(less).append(p)
    return temp.extend(quicksort(greater))

# median-of-three pivot
def pivot(one, two, two_i, three):
    if one < two < three:
        return two, two_i
    elif two < one < three:
        return one, 0
    return three, -1


def heapsort():
    return
