# 23. Merge k Sorted Lists
# https://leetcode.com/problems/merge-k-sorted-lists/description/

from typing import List
import heapq


class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next


class ListNodeExtension(ListNode):
    def __lt__(self, other):
        return self.val < other.val


class Solution:
    def mergeKLists(self, lists: List[ListNode]) -> ListNode:
        ListNode.__lt__ = ListNodeExtension.__lt__
        heap = []
        for head in lists:
            if head:
                heapq.heappush(heap, head)

        dummy = tail = ListNode(0)
        while heap:
            curr = heapq.heappop(heap)
            tail.next = curr
            tail = tail.next
            if curr.next:
                heapq.heappush(heap, curr.next)

        return dummy.next
