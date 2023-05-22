# 358. Rearrange String k Distance Apart
# https://leetcode.com/problems/rearrange-string-k-distance-apart/description/
import collections
import heapq


class Solution:
    def rearrangeString(self, s: str, k: int) -> str:

        if k==0:
            return s

        cnt = collections.Counter(s)
        max_heap = []
        for letter, freq in cnt.items():
            max_heap.append((-freq, letter))
        heapq.heapify(max_heap)
        cooldown_queue = collections.deque()
        res = []

        while max_heap:
            item = heapq.heappop(max_heap)
            freq, letter = -item[0], item[1]
            res.append(letter)
            freq -= 1
            cooldown_queue.append((-freq, letter))
            if len(cooldown_queue) >= k:
                front = cooldown_queue.popleft()
                if front[0]:
                    heapq.heappush(max_heap, front)

        return ''.join(res) if len(res) == len(s) else ''
