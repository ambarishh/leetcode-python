# 155. Min Stack
# https://leetcode.com/problems/min-stack/description/
# https://leetcode.com/problems/min-stack/solutions/49234/python-easy-to-understand-solution-using-two-stacks/
import collections


class MinStack:

    def __init__(self):
        self.stack = collections.deque([])
        self.min_stack = collections.deque([])

    def push(self, val: int) -> None:
        self.stack.append(val)
        # if empty or LE
        if len(self.min_stack) == 0 or val <= self.min_stack[-1]:
            self.min_stack.append(val)

    def pop(self) -> None:
        val = self.stack.pop()
        if self.min_stack[-1] == val:
            self.min_stack.pop()

    def top(self) -> int:
        return self.stack[-1]

    def getMin(self) -> int:
        return self.min_stack[-1]
