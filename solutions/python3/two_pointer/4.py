# 844. Backspace String Compare
# https://leetcode.com/problems/backspace-string-compare/description/

class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:

        idx1, idx2 = len(s) - 1, len(t) - 1

        def next_index(idx:int, p:str):
            back_space_count = 0
            while idx >= 0:
                if p[idx] == '#':
                    back_space_count += 1
                    idx -= 1
                elif back_space_count > 0: # imp to check a#b# in one pass
                    back_space_count -= 1
                    idx -= 1
                else:
                    break
            return idx

        while idx1 >= 0 or idx2 >= 0:

            idx1 = next_index(idx1, s)
            idx2 = next_index(idx2, t)

            # reached end of both strings
            if idx1 < 0 and idx2 < 0:
                return True

            # reached end of one string
            if idx1 < 0 or idx2 < 0:
                return False

            if s[idx1] != t[idx2]:
                return False

            idx1 -= 1
            idx2 -= 1

        return True
