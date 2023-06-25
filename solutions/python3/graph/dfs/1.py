# 200. Number of Islands
# https://leetcode.com/problems/number-of-islands/description/
from typing import List


class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:

        if not grid:
            return 0

        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        count = 0

        def dfs(row: int, col: int):
            if ( row < 0 or row >= ROWS
                    or col < 0 or col >= COLS
                    or grid[row][col] == "0"
                    or (row, col) in visited):
                return

            # else visit
            visited.add((row, col))
            # visit neighbors
            dfs(row - 1, col)
            dfs(row + 1, col)
            dfs(row, col - 1)
            dfs(row, col + 1)

        for row in range(ROWS):
            for col in range(COLS):
                if grid[row][col] == "1" and (row, col) not in visited:
                    count += 1
                    dfs(row, col)

        return count
