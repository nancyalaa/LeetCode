class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        L = []
        for i in accounts:
            s = 0
            for j in i:
                s += j
            L.append(s)
        return max(L)
                
        