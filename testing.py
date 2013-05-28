import time
from algorithms import *

def read(size):
    array = []
    # open file and read $size lines
    of = open("100million.txt", "r")
    for i in range(0,size):
        array.append(of.readline())
    of.close()
    return array

def sort(array, t, size):
    # start timer and run over $sort algorithm
    target = sorted(array)
    start = time.time()
    if t == "mergesort":
        array = mergesort(array)
    elif t == "quicksort":
        array = quicksort(array)
    else:
        array = heapsort(array)
    # stop timer and save time to results file
    stop = time.time()
    assert array == target
    return str(t +" "+ str(size) +" "+ str(stop - start)+'\n')

def save(result, t):
    of = open(t+".txt", "a")
    of.write(result)
    of.close()

def truerandom(size, t):
    array = read(size)
    save(sort(array, t, size), "truerandom")

def reversesort(size, t):
    array = reversed(sorted(read(size)))
    save(sort(array, t, size), "reversesort")

def duplicates(size, t):
    array = read(size)
    # repeats of a few data points
    save(sort(array, t, size), "duplicates")

def inorder(size, t):
    array = sorted(read(size))
    save(sort(array, t, size), "inorder")
