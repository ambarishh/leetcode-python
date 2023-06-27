# 323. Number of Connected Components in an Undirected Graph
# https://leetcode.com/problems/number-of-connected-components-in-an-undirected-graph/description/
import collections
from typing import List


class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        graph = collections.defaultdict(list)
        visited = set()
        count = 0

        for x,y in edges:
            graph[x].append(y)
            graph[y].append(x)

        def dfs(node:int):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        for x in range(n):
            if x not in visited:
                count += 1
                dfs(x)

        return count

