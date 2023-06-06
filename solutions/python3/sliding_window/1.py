# 438. Find All Anagrams in a String
# https://leetcode.com/problems/find-all-anagrams-in-a-string/description/
from collections import defaultdict
from typing import List


class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        char_freq_map = defaultdict(int)
        for c in p:
            char_freq_map[c] += 1

        res, formed, window_start = [], 0, 0

        for window_end in range(len(s)):
            letter = s[window_end]
            if letter in char_freq_map:
                char_freq_map[letter] -= 1
                if char_freq_map[letter] == 0:
                    formed += 1

            # slide the window
            window_len = window_end-window_start+1
            if window_len > len(p):
                letter_remove = s[window_start]
                if letter_remove in char_freq_map:
                    if char_freq_map[letter_remove] == 0:
                        formed -= 1
                    char_freq_map[letter_remove] += 1
                window_start += 1

            #print(char_freq_map)

            # all chars found
            if formed == len(char_freq_map):
                res.append(window_start)

        return res


def main():
    solution = Solution()
    s = "cbaebabacd"
    p = "abc"
    ans = solution.findAnagrams(s,p)
    print(ans)


if __name__ == "__main__":
    main()
