import time
from algorithms import *
def truerandom(size, sort):
    array = []
    # open file and read $size lines
    of = open("4.txt", "r")
    for i in range(0,size):
        array.append(of.readline())
    of.close()
    # start timer and run over $sort algorithm
    start = time.time()
    if sort == "mergesort":
        mergesort(array)
    elif sort == "quicksort":
        quicksort(array)
    else:
        heapsort(array)
    # stop timer and save time to results file
    stop = time.time()
    of = open("truerandom.txt", "a")
    of.write(sort +" "+ str(size) +" "+ str(stop - start)+'\n')
    of.close()

def reversesort(size, sort):
    pass

def nearsorted(size, sort):
    pass

def duplicates(size, sort):
    pass

def sorted(size, sort):
    pass
