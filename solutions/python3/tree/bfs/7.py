# 314. Binary Tree Vertical Order Traversal
# https://leetcode.com/problems/binary-tree-vertical-order-traversal/
from collections import defaultdict, deque
from typing import Optional, List

from solutions.python3.tree.dfs.utils import TreeNode


class Solution:
    def verticalOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        idx_node_map = defaultdict(list)
        if not root:
            return []

        queue = deque([(root,0)])

        while queue:
            size = len(queue)
            for _ in range(size):
                (node, idx) = queue.popleft()
                # add node to idx
                idx_node_map[idx].append(node.val)
                if node.left:
                    queue.append((node.left, idx-1))
                if node.right:
                    queue.append((node.right, idx+1))

        return [idx_node_map[idx] for idx in sorted(idx_node_map.keys())]

