# 1730. Shortest Path to Get Food
# https://leetcode.com/problems/shortest-path-to-get-food/description/
import collections
from typing import List


class Solution:
    def getFood(self, grid: List[List[str]]) -> int:
        if not grid:
            return -1
        ROWS, COLS = len(grid), len(grid[0])
        visited = set()
        # since shortest dist, use BFS
        queue = collections.deque()
        DIRS = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        # find the start cell
        def findStart():
            for r in range(ROWS):
                for c in range(COLS):
                    if grid[r][c] == '*':
                        return (r, c)
            # throw error

        def withinBounds(r: int, c: int):
            if (0 <= r < ROWS
                    and 0 <= c < COLS):
                return True
            return False

        # instead of break statement
        (r, c) = findStart()
        queue.append((r, c, 0))
        visited.add((r, c))

        while queue:
            (r, c, dist) = queue.popleft()


            for direction in DIRS:
                new_r = r + direction[0]
                new_c = c + direction[1]
                # check in valid cell
                if (
                        not withinBounds(new_r, new_c)
                        or grid[new_r][new_c] not in ["O", '#']
                        or visited in (new_r, new_c)
                ):
                    continue
                # found food
                if grid[new_r][new_c] == '#':
                    return dist + 1
                queue.append((new_r, new_c, dist + 1))
                visited.add((new_r, new_c))

        return -1

solution = Solution()
matrix = [["X","X","X","X","X","X"],["X","*","O","O","O","X"],["X","O","O","#","O","X"],["X","X","X","X","X","X"]]
print(solution.getFood(matrix))

# the question is whether you should
#
# (a) first mark the neighbors as visited and then queue them, or
# (b) first queue them, and only mark cells as visited after they have been popped from the queue.

#If performance doesn't matter, both are ok. However in practice (a) is much faster (in fact, b even times out),
# and here's why: you'll want to mark the cells as visited as soon as possible,
# and that's because the next element you pop from the queue might be looking at the same neighbors,
# and you want to avoid queuing the same cells multiple times.