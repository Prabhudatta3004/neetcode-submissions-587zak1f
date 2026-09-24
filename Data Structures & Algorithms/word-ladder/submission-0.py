from collections import deque
from string import ascii_lowercase

class Solution:
    def ladderLength(
        self, beginWord: str, endWord: str, wordList: List[str]
    ) -> int:
        remaining = set(wordList)

        if endWord not in remaining:
            return 0

        queue = deque([(beginWord, 1)])
        remaining.discard(beginWord)

        while queue:
            word, length = queue.popleft()

            if word == endWord:
                return length

            for i in range(len(word)):
                for ch in ascii_lowercase:
                    candidate = word[:i] + ch + word[i + 1:]

                    if candidate in remaining:
                        remaining.remove(candidate)
                        queue.append((candidate, length + 1))

        return 0