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


array = [4, 9, 10, 44, 13, 1, 7]
array = mergesort(array)
print(array)
