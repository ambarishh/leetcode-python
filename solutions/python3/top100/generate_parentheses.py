from typing import List


class Solution:

    def generateParenthesis(self, n: int) -> List[str]:
        res = []

        def dfs(open_b: int, closed_b: int, ans: str) -> None:

            if len(ans) == n * 2:
                res.append(ans)

            if open_b < n:
                dfs(open_b + 1, closed_b, ans + "(")

            if closed_b < open_b:
                dfs(open_b, closed_b + 1, ans + ")")

        dfs(0, 0, "")
        return res
