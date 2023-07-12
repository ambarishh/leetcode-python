# 127. Word Ladder
# https://leetcode.com/problems/word-ladder/description/
# Soln-https://leetcode.com/problems/word-ladder/solutions/346920/python3-breadth-first-search/
import collections
from typing import List


class Solution:
    def ladderLength(self, beginWord: str, endWord: str, wordList: List[str]) -> int:

        if endWord not in wordList:
            return 0

        # construct graph
        graph = collections.defaultdict(list)
        for word in wordList:
            for i in range(len(word)):
                interim_word = word[:i] + "*" + word[i + 1:]
                graph[interim_word].append(word)
        # '*ot': ['hot', 'dot', 'lot'],
        # 'h*t': ['hot'],
        # 'ho*': ['hot'],
        # 'd*t': ['dot'], 'do*': ['dot', 'dog'], '*og': ['dog', 'log', 'cog'], 'd*g': ['dog'], 'l*t': ['lot'], 'lo*': ['lot', 'log'], 'l*g': ['log'], 'c*g': ['cog'], 'co*': ['cog']})

        # bfs
        visited = set()
        queue = collections.deque([])
        queue.append(beginWord)
        visited.add(beginWord)
        dist = 1

        while queue:
            # we need to track level now
            L = len(queue)
            for _ in range(L):
                word = queue.popleft()
                for i in range(len(word)):
                    interim_word = word[:i] + "*" + word[i + 1:]
                    for neighbor in graph[interim_word]:
                        if neighbor == endWord:
                            return dist + 1
                        if neighbor in visited:
                            continue
                        visited.add(neighbor) # imp or TLE
                        queue.append(neighbor)
            dist += 1

        return 0


beginWord = "hit"
endWord = "cog"
wordList = ["hot", "dot", "dog", "lot", "log", "cog"]

s = Solution()
ans = s.ladderLength(beginWord, endWord, wordList)
print(ans)