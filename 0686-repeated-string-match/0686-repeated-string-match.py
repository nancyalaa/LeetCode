class Solution:
    def repeatedStringMatch(self, a: str, b: str) -> int:
        if a.find(b) > - 1: return 1 
        counter = 1
        temp = a
        while len(temp) <= 2*(max(len(a), len(b))):
            temp += a
            counter += 1
            if temp.find(b) > - 1: return counter
        return -1
            
            
        