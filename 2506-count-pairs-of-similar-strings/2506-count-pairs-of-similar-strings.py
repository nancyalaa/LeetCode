class Solution:
    def similarPairs(self, words: List[str]) -> int:
        counter = 0
        for idx1 in range(len(words)-1):
            for idx2 in range(idx1+1, len(words)):
                if set(words[idx1]) == set(words[idx2]): counter += 1
        return counter
        