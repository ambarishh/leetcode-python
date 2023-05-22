# Maximum distinct elements after removing k elements
# https://www.geeksforgeeks.org/maximum-distinct-elements-removing-k-elements/#
import heapq
from collections import Counter


def maxDistinctNum(a, k):
    cnt = Counter(a)
    heap = []
    unique_ele = 0
    # add duplicate ele to heap
    for key, value in cnt.items():
        if value > 1:
            heap.append((value, key))
        else:
            unique_ele += 1
    # convert to min heap
    heapq.heapify(heap)

    # remove smaller freq ele first
    while heap and k:
        (value, key) = heapq.heappop(heap)
        value = value - 1
        if value == 1:
            unique_ele += 1
        else:
            heapq.heappush(heap, (value, key))
        k -= 1

    # if k is not zero
    if k:
        unique_ele -= k

    return unique_ele


# Driver Code
if __name__ == "__main__":
    # Array
    arr = [5, 7, 5, 5, 1, 2, 2]
    K = 3

    # Function Call
    print("Maximum distinct elements = ", maxDistinctNum(arr, K))
