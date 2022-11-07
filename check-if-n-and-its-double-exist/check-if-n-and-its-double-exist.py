class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        if arr.count(0) >= 2:
            return True
        for i in arr:
            for j in arr:
                if (i != j) and (i !=0 and j != 0) and (i / j == 2 or j / i == 2) :
                    return True
        return False
        