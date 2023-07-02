# 417. Pacific Atlantic Water Flow
# https://leetcode.com/problems/pacific-atlantic-water-flow/description/
from typing import List


class Solution:
    def pacificAtlantic(self, heights: List[List[int]]) -> List[List[int]]:

        if not heights:
            return [[]]

        ROWS, COLS = len(heights), len(heights[0])
        DIRS = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        # visited also stores all cells which satisfy our traversal requirements
        visited_atlantic = set()
        visited_pacific = set()

        def withinBounds(r, c):
            if r < 0 or r >= ROWS or c < 0 or c >= COLS:
                return False
            return True

        def dfs(r: int, c: int, visited: set):

            if (r, c) in visited:
                return

            visited.add((r, c))

            for direction in DIRS:
                new_r, new_c = r + direction[0], c + direction[1]
                # if (
                #         not withinBounds(new_r, new_c)
                #         or (new_r, new_c) in visited
                #         or heights[new_r][new_c] <= heights[r][c]
                # ):
                #     return  #bug here is it does not check for remaining directions. use continue
                dfs(new_r, new_c, visited)
                if (withinBounds(new_r, new_c)
                        and heights[new_r][new_c] >= heights[r][c]
                ):
                    dfs(new_r, new_c, visited)

        # begin traversal
        for r in range(ROWS):
            dfs(r, 0, visited_pacific)
            dfs(r, COLS - 1, visited_atlantic)

        for c in range(COLS):
            dfs(0, c, visited_pacific)
            dfs(ROWS - 1, c, visited_atlantic)

        return list(visited_atlantic.intersection(visited_pacific))
