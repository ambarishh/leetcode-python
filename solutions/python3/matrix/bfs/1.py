# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/
import collections
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        DIRS = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        islands = 0
        visited = set()
        queue = collections.deque()

        def withinBounds(r: int, c: int) -> bool:
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return False
            return True

        def bfs(r, c):
            queue.append((r, c))
            while queue:
                (x, y) = queue.popleft()
                for dx, dy in DIRS:
                    new_x = x + dx
                    new_y = y + dy
                    if (
                            not withinBounds(new_x, new_y)
                            or grid[new_x][new_y] == "0"
                            or (new_x, new_y) in visited  #vimp to make traversal efficient
                    ):
                        continue
                    queue.append((new_x, new_y))
                    visited.add((new_x,new_y))

        for r in range(ROWS):
            for c in range(COLS):
                if grid[r][c] == "0":
                    continue
                if (r, c) in visited:
                    continue
                islands += 1
                bfs(r, c)

        return islands
