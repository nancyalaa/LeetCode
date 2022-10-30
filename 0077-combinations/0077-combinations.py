class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        L = []
        for i in range(1,n+1):
            L.append(i)
        return list(combinations(L,k))
                