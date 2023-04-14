from typing import List
from merge_two_sorted_lists import ListNode
import heapq


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
