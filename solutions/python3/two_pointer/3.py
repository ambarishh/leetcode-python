# 11. Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        left,right = 0, len(height)-1
        maxArea = 0

        while(left<=right):
            width = right-left
            currArea = width * min(height[left], height[right])
            maxArea = max(maxArea, currArea)

            if(height[left] < height[right]):
                left += 1
            else:
                right -= 1

        return maxArea