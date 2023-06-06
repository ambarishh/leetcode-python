# 111. Minimum Depth of Binary Tree
# https://leetcode.com/problems/minimum-depth-of-binary-tree/description/
from collections import deque
from typing import Optional

from solutions.python3.tree.dfs.utils import TreeNode


class Solution:
    def minDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        queue = deque([root])
        level = 0
        while queue:
            level+=1
            size = len(queue)
            for _ in range(size):
                node = queue.popleft()
                if not node.left and not node.right:  #leaf node
                    return level
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)

