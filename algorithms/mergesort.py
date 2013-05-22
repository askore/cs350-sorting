def merge(left, right):
    return left.extend(right) # TODO: implement me

def mergesort(array):
    length = len(array)
    mid = int(length / 2)
    if length <= 1:
        return array
    # this is black magic and stands in place of n assignments
    left = array[0:mid]
    right = array[mid+1:length]
    left = mergesort(left)
    right = mergesort(right)
    return merge(left, right)


array = [4, 9, 10, 44, 13, 1, 7]
mergesort(array)
print(array)
