class Solution:
    def countWords(self, words1: List[str], words2: List[str]) -> int:
        counter = 0 
        for i in words2:
            if words1.count(i) == 1 and words2.count(i) == 1:
                counter += 1
        return counter
        