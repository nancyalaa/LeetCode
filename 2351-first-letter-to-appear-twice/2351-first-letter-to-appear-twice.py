class Solution:
    def repeatedCharacter(self, s: str) -> str:
        res = []
        for i in s:
            if i not in res:
                res.append(i)
            else:
                return i
                
        