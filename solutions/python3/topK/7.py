# Sum of all elements between k1’th and k2’th smallest elements
# https://www.geeksforgeeks.org/sum-elements-k1th-k2th-smallest-elements/#
import heapq


def sumBetweenTwoKth(arr, k1, k2):

    sum=0
    min_heap=[]
    for num in arr:
        heapq.heappush(num)
        if len(min_heap) > k2 :
            heapq.heappop(min_heap)

    for i in range(k1,k2):
        sum += heapq.heappop(min_heap)

    return sum
