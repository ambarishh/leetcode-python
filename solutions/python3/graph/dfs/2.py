# 261. Graph Valid Tree
# https://leetcode.com/problems/graph-valid-tree/description/
import collections
from typing import List


class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        if len(edges) != n - 1:
            return False

        graph = collections.defaultdict(list)
        visited = set()

        for x, y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(node: int):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        # 0 is the root
        dfs(0)

        return n == len(visited)
