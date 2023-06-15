# 199. Binary Tree Right Side View
# https://leetcode.com/problems/binary-tree-right-side-view/
from collections import deque
from typing import Optional, List

from solutions.python3.tree.dfs.utils import TreeNode


class Solution:
    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []

        queue, res = deque([root]), []
        while queue:
            size = len(queue)
            for idx in range(size):
                node = queue.popleft()
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
                if idx == size - 1:
                    res.append(node.val)

        return res
