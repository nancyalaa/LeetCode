class Solution:
    def countPrefixes(self, words: List[str], s: str) -> int:
        counter = 0
        for word in words:
            if s.find(word) == 0: counter += 1
        return counter
        