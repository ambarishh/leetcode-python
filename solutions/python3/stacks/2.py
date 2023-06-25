# 71. Simplify Path
# https://leetcode.com/problems/simplify-path/description/
from collections import deque


class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = deque()
        for fileName in path.split('/'):
            if stack and fileName == "..":
                stack.pop()
            elif fileName in ["", ".", ".."]:
                continue
            else:
                stack.append(fileName)

        return '/' + '/'.join(stack)
