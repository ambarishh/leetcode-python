# 129. Sum Root to Leaf Numbers
# https://leetcode.com/problems/sum-root-to-leaf-numbers/description/
from typing import Optional


# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right


class Solution:
    def sumNumbers(self, root: Optional[TreeNode]) -> int:
        def dfs(root, curr):
            if not root:
                return 0
            sum = curr * 10 + root.val
            #  root to leaf path completed
            if not root.left and not root.right:
                return sum
            # add leaf nodes
            return dfs(root.left, sum) + dfs(root.right, sum)

        return dfs(root, 0)
