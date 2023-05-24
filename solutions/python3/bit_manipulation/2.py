# 338. Counting Bits
# https://leetcode.com/problems/counting-bits/description/

from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        res = [0]
        for i in range(1, n+1):
            # bit(m) = bit(m>>1) + last_bit_of_m
            # m>>1 == m//2 (right shift by 1 = divided by 2)
            cnt = res[i>>1] + (i&1)
            res.append(cnt)
        return res