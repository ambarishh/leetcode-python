# 977. Squares of a Sorted Array
# https://leetcode.com/problems/squares-of-a-sorted-array/
from typing import List


class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        left = 0
        right = n-1

        for i in range(n-1, -1, -1):
            left_num = nums[left]
            right_num = nums[right]
            if abs(left_num) > abs(right_num):
                num = left_num
                left += 1
            else:
                num = right_num
                right -= 1
            res[i] = num*num
        return res

        