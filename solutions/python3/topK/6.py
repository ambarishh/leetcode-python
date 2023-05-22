# 451. Sort Characters By Frequency
# https://leetcode.com/problems/sort-characters-by-frequency/
import heapq
from collections import Counter


class Solution:
    def frequencySort(self, s: str) -> str:
        cnt = Counter(s)
        max_heap = [(-1 * freq, c) for c, freq in cnt.items()]
        heapq.heapify(max_heap)
        res=[]
        while max_heap:
            (freq,c) = heapq.heappop(max_heap)
            res += -freq*c
        return ''.join(res)