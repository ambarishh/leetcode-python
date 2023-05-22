# 1167. Minimum Cost to Connect Sticks
# https://leetcode.com/problems/minimum-cost-to-connect-sticks/description/
import heapq
from typing import List


class Solution:
    def connectSticks(self, sticks: List[int]) -> int:
        heapq.heapify(sticks)
        res=0
        while len(sticks) > 1:
            x, y = heapq.heappop(sticks), heapq.heappop(sticks)
            res += x+y
            heapq.heappush(sticks, x+y)
        return res