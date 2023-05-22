# 191. Number of 1 Bits
# https://leetcode.com/problems/number-of-1-bits/description/
class Solution:
    def hammingWeight(self, n: int) -> int:
        # return bin(n).count(1)
        ans = 0
        while n:
            n = n & (n-1)
            ans = ans + 1
        return ans
