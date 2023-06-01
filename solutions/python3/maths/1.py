# 1523. Count Odd Numbers in an Interval Range
# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/description/
# https://leetcode.com/problems/count-odd-numbers-in-an-interval-range/solutions/754708/python3-one-liner-explanation/
class Solution:
    def countOdds(self, low: int, high: int) -> int:
        return (high-low+1)//2 + (high%2 and low%2)