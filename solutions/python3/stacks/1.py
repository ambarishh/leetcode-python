# 20. Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
from collections import deque


class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        closed_open_map = {'}': '{', ')':'(', ']':'['}

        for c in s:
            # open bracket
            if c in closed_open_map.values():
                stack.append(c)
            else:
                if len(stack) == 0:
                    return False
                open_actual = stack.pop()
                open_expected = closed_open_map.get(c)
                if open_actual != open_expected:
                    return False

        return len(stack) == 0
