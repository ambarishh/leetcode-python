from typing import List


class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        mapping = {'0': '', '1': '', '2': 'abc', '3': 'def', '4': 'ghi', '5': 'jkl',
                   '6': 'mno', '7': 'pqrs', '8': 'tuv', '9': 'wxyz'}
        from collections import deque
        q = deque()
        q.append('')
        result = []
        index = 0

        while q:
            length = len(q)
            for _ in range(length):
                combo = q.popleft()
                # print(combo)
                if len(combo) == len(digits):
                    result.append(combo)
                else:
                    digit = digits[index]
                    letters = mapping[digit]
                    for letter in letters:
                        q.append(combo + letter)
            index += 1

        # if empty
        return result if digits else []


def main():
    solution = Solution()
    digits = "9"
    ans = solution.letterCombinations(digits)
    print(ans)


if __name__ == "__main__":
    main()
