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
        left.reverse()
        merged_list.extend(left)
    else:
        right.reverse()
        merged_list.extend(right)
    return merged_list

# recursive part of mergesort
def mergesort(array):
    length = len(array)
    if length <= 1:
        return array
    mid = length // 2
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
    if one < two:
        if two < three:
            return two, two_i
        else:
            if three < one:
                return one, 0
            else:
                return three, -1
    else:
        if one < three:
            return one, 0
        else:
            if three < two:
                return two, two_i
            else:
                return three, -1



def siftDown(array, start, end):
    while start * 2 <= end:
        child = start * 2 + 1
        swap = start * 2
        if swap == end or array[swap] > array[child]:
            child = swap

        if array[start] < array[child]:
            array[start], array[child] = array[child], array[start]
            start = child
        else:
            return array
    return array

def heapsort(array):
    length = len(array)

    start = (length - 1) // 2
    while start >= 0:
        siftDown(array, start, length - 1)
        start -= 1

    end = length - 1
    while end > 0:
        array[end], array[0] = array[0], array[end]
        end -= 1
        siftDown(array, 0, end)
    return array
