# 1319. Number of Operations to Make Network Connected
# https://leetcode.com/problems/number-of-operations-to-make-network-connected/description/
import collections
from typing import List


class Solution:
    # if there are at least n - 1 edges,
    # the solution is the number of connected components minus one.
    # Otherwise, we return -1.
    def makeConnected(self, n: int, connections: List[List[int]]) -> int:
        numberOfEdges = len(connections)
        if numberOfEdges != n - 1:  #imp less than and not equal
            return -1

        graph = collections.defaultdict(list)
        visited = set()

        for a, b in connections:
            graph[a].append(b)
            graph[b].append(a)

        def dfs(node: int):
            if node in visited:
                return
            visited.add(node)
            for neighbor in graph[node]:
                if neighbor not in visited:
                    dfs(neighbor)

        connectedComponents = 0
        for i in range(n):
            if i not in visited:
                connectedComponents += 1
                dfs(i)

        return connectedComponents - 1
