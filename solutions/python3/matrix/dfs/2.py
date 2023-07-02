# 329. Longest Increasing Path in a Matrix
# https://leetcode.com/problems/longest-increasing-path-in-a-matrix/description/
from typing import List


class Solution:
    def longestIncreasingPath(self, matrix: List[List[int]]) -> int:
        if not matrix:
            return 0
        ROWS, COLS = len(matrix), len(matrix[0])
        cache = [[0] * COLS for _ in range(ROWS)]

        def withinBoundary(r: int, c: int) -> bool:
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return False
            else:
                return True

        def dfs(r: int, c: int) -> int:
            if not withinBoundary(r, c):
                return 0
            if cache[r][c]:
                return cache[r][c]
            val = matrix[r][c]
            up = dfs(r - 1, c) if withinBoundary(r - 1, c) and matrix[r - 1][c] > val else 0
            down = dfs(r + 1, c) if withinBoundary(r + 1, c) and matrix[r + 1][c] > val else 0
            left = dfs(r, c - 1) if withinBoundary(r, c - 1) and matrix[r][c - 1] > val else 0
            right = dfs(r, c + 1) if withinBoundary(r, c + 1) and matrix[r][c + 1] > val else 0
            #important to set cache here
            cache[r][c] = 1 + max(up, down, left, right)
            return cache[r][c]

        res = 0
        for r in range(ROWS):
            for c in range(COLS):
                res = max(res, dfs(r, c))

        return res


solution = Solution()
matrix = [[9, 9, 4], [6, 6, 8]]
print(solution.longestIncreasingPath(matrix))
