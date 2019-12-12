# Created by Alejandro at 
# 9/7/2019
"""
# Descriptions
Modify the quicksort function (found in the file testquicksort.py), so that it calls insertionSort
(found in the file algorithms.py) to sort any sublist whose size is less than 50 items. Compare the performance of this
version with that of the original one, using data sets of 50, 500, and 5000 items. Then, adjust the threshold for using
the insertion sort to determine an optimal setting.

Profiler was written by the textbook author, Lambert
"""
import quicksort as qs
from algorithms import insertionSort
from profiler import Profiler

def modifiedQuicksort(lyst,threshold):
    p = Profiler()
    if len(lyst) <= threshold: #I took the instructions to mean less than or equal to because the testing phase is with
        # data of 50 to 5000... use variable to make the threshold editable from the testing side.
        p.test(insertionSort, lyst=lyst, size=len(lyst), comp=False,
               exch=False, trace=False)
    else:
        p.test(qs.quicksort,lyst=lyst, size=len(lyst), comp=False,
               exch=False, trace=False)


import random

#driver program to test

def main(size = 50, threshold = 50, sort = modifiedQuicksort):
    """Driver function to test and analyze different sorting methods."""
    print("threshold size is now: " + str(threshold))

    size = 50
    lyst = []
    for count in range(size):
        lyst.append(random.randint(1, size + 1))
    sort(lyst,threshold)

    size = 500
    lyst = []
    for count in range(size):
        lyst.append(random.randint(1, size + 1))
    sort(lyst,threshold)

    size = 5000
    lyst = []
    for count in range(size):
        lyst.append(random.randint(1, size + 1))
    sort(lyst,threshold)

    x =   """
    I found insertsearch performs better the smaller the size of the list is. Performance diminished at around list 
    size 100
    you can see at problem size 150, performance is around .002 lapse seconds. Quicksort tends to be .001 at this 
    problem size.
    """
    print(x)
    threshold = 150
    print("threshold size is now: " + str(threshold))
    size = 50
    lyst = []
    for count in range(size):
        lyst.append(random.randint(1, size + 1))
    sort(lyst, threshold)

    size = 75
    lyst = []
    for count in range(size):
        lyst.append(random.randint(1, size + 1))
    sort(lyst, threshold)

    size = 100
    lyst = []
    for count in range(size):
        lyst.append(random.randint(1, size + 1))
    sort(lyst, threshold)

    size = 150
    lyst = []
    for count in range(size):
        lyst.append(random.randint(1, size + 1))
    sort(lyst, threshold)


if __name__ == "__main__":
    main()