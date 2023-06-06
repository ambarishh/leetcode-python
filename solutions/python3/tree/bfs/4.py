# 637. Average of Levels in Binary Tree
# https://leetcode.com/problems/average-of-levels-in-binary-tree/
from collections import deque
from typing import Optional, List
from solutions.python3.tree.dfs.utils import TreeNode


class Solution:
    def averageOfLevels(self, root: Optional[TreeNode]) -> List[float]:
        if not root:
            return 0
        queue, res = deque([root]), []
        while queue:
            level = []
            size = len(queue)
            sum = 0
            for _ in range(size):
                node = queue.popleft()
                sum += node.val
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            res.append(sum/size)
        return res
