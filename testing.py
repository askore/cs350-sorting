import time
import os
from algorithms import *

def read(size):
    array = []
    # open file and read $size lines
    of = open("data/100million.txt", "r")
    for i in range(0,size):
        array.append(of.readline())
    of.close()
    return array

def sort(array, alg):
    # start timer and run over $sort algorithm
    target = sorted(array)
    start = time.time()
    if alg == "mergesort":
        array = mergesort(array)
    elif alg == "quicksort":
        array = quicksort(array)
    elif alg == "heapsort":
        array = heapsort(array)

    # stop timer and save time to results file
    stop = time.time()
    elapsedtime = stop - start
    # verify sort success
    assert array == target
    return elapsedtime

def save(alg, elapsedtime, size, datatype):
    d = os.path.join(".", "results")
    filename = os.path.join(d, datatype + ".csv")
    if not os.path.isdir(d):
        os.makedirs(d)
    if not os.path.isfile(filename):
        of = open(filename, "w")
        of.write("Algorithm,Number of elements,Time elapsed (sec)\n")
    else:
        of = open(filename, "a")
    of.write(alg + "," + str(size) + "," + str(elapsedtime) + "\n")
    of.close()

def truerandom(size, alg):
    array = read(size)
    time = sort(array, alg)
    save(alg, time, size, "truerandom")

def reversesort(size, alg):
    array = sorted(read(size))
    array.reverse()
    time = sort(array, alg)
    save(alg, time, size, "reversesort")

def duplicates(size, alg):
    array = read(size)
    # repeats of a few data points
    time = sort(array, alg)
    save(alg, time, size, "duplicates")

def inorder(size, alg):
    array = sorted(read(size))
    time = sort(array, alg)
    save(alg, time, size, "inorder")
