class Solution:
    def getPermutation(self, n: int, k: int) -> str:
        strOfNums = ''.join(str(e) for e in list(range(1,n+1)))
        permList = [''.join(p) for p in permutations(strOfNums)]
        return permList[k-1]