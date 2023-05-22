# 347. Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/description/
import heapq
from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        cnt = Counter(nums)
    #     cnt.most_common(k)
    #     num_freq_map = {}
    #     for num in nums:
    #         if num in num_freq_map:
    #             num_freq_map[num] += -1
    #         else:
    #             num_freq_map[num] = -1

        heap = [(-1 * freq, num) for num, freq in cnt.items()]
        heapq.heapify(heap)

        res = []
        for i in range(k):
            (_, num) = heapq.heappop(heap)
            res.append(num)
        return res
