class Solution:
    def divisibilityArray(self, word: str, m: int) -> List[int]:
        output = [0]*len(word)
        prefix = 0
        for i in range(len(word)):
            prefix = (10*prefix + int(word[i])) % m
            if prefix % m == 0: output[i] = 1
        return output
            
        