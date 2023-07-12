# 133. Clone Graph
# https://leetcode.com/problems/clone-graph/
import collections


# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []


class Solution:
    def cloneGraph(self, node: 'Node') -> 'Node':
        if not node:
            return node

        visited = {}
        visited[node] = Node(node.val)

        queue = collections.deque([node])

        while queue:
            n = queue.popleft()
            # for _ in range(len(queue)) -> if we care about the level
            cloned_n = visited[n]
            for neighbor in n.neighbors:
                if neighbor not in visited.keys():
                    visited[neighbor] = Node(neighbor.val)
                    queue.append(neighbor)
                cloned_neighbor = visited[neighbor]
                cloned_n.neighbors.append(cloned_neighbor)

        return visited[node]



