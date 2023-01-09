class Solution:
    def numOfStrings(self, patterns: List[str], word: str) -> int:
        counter = 0
        for substring in patterns:
            if substring in word: counter += 1
        return counter
        