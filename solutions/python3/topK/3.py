# 973. K Closest Points to Origin
# https://leetcode.com/problems/k-closest-points-to-origin/
import heapq
from typing import List


class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        max_heap = []
        for point in points:
            dist = point[0]*point[0] + point[1]*point[1]
            heapq.heappush(max_heap, (-1*dist, point))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return [tuple[1] for tuple in max_heap]
