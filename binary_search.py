
# give me a sorted list, ill find the index of your target in that list
import time
import random
from unittest.util import sorted_list_difference
# binary search
def b_search(l, target, low=None, high=None):

    if low is None:
        low = 0
    if high is None:
        high = len(l)-1 

    if high < low:
        return -1

    guess =  (low + high) // 2

    if l[guess] == target:
        return guess

    elif l[guess] > target:
        
        return b_search(l, target, low, guess - 1)

    
    return b_search(l, target, guess + 1, high)

# -1 is returned if the target is not found
def naive_search(l, target):
    for i in range(len(l)):
        if l[i] == target:
            return i

    return -1


if __name__ == '__main__':
    size = 10000
    sortedList = set()
    while len(sortedList) < size:
        sortedList.add(random.randint(-size, size))

    sortedList = sorted(list(sortedList))

    start = time.time()
    for needle in sortedList:
        naive_search(sortedList, needle)
    print(f"that took {time.time()-start} seconds")
    
    start = time.time()
    for needle in sortedList:
        b_search(sortedList, needle)
    print(f"that took {time.time()-start} seconds")