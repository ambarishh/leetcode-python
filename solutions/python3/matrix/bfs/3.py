# 286. Walls and Gates
# https://leetcode.com/problems/walls-and-gates/description/
import collections
from typing import List

#Start BFS from all gates at once
class Solution:
    def wallsAndGates(self, rooms: List[List[int]]) -> None:
        """
        Do not return anything, modify rooms in-place instead.
        """
        EMPTY = 2147483647
        GATE = 0

        if not rooms:
            return

        ROWS,COLS = len(rooms), len(rooms[0])
        queue = collections.deque([])
        DIRS = [(-1, 0), (1, 0), (0, 1), (0, -1)]

        for r in range(ROWS):
            for c in range(COLS):
                if rooms[r][c] == GATE:
                    queue.append((r,c))


        while queue:
            (r,c) = queue.popleft()

            for direction in DIRS:
                nr = r + direction[0]
                nc = c + direction[1]

                if 0<=nr<ROWS and 0<=nc<COLS and rooms[nr][nc]==EMPTY:
                    rooms[nr][nc]=rooms[r][c]+1
                    queue.append((nr,nc))


