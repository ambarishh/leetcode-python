# 767. Reorganize String
# https://leetcode.com/problems/reorganize-string/
import heapq
from collections import Counter


class Solution:
    # @staticmethod
    def reorganizeString(self, s: str) -> str:
        cnt = Counter(s)
        max_heap = [(-freq, c) for c, freq in cnt.items()]
        res = []
        heapq.heapify(max_heap)
        prev_ele = None

        while max_heap:
            curr = heapq.heappop(max_heap)
            freq, c = -curr[0], curr[1]
            res.append(c)
            freq -= 1
            if prev_ele:
                heapq.heappush(max_heap, prev_ele)

            if freq:
                prev_ele = (-freq, c)
            else:
                prev_ele = None

        ans = ''.join(res)

        return ans if len(ans) == len(s) else ''


def main():
    s = "aab"
    solution = Solution()
    # Function Call
    print("Reorganized String    = ", solution.reorganizeString(s))


# Driver Code
if __name__ == "__main__":
    main()
