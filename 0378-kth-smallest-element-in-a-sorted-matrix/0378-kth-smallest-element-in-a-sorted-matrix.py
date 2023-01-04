class Solution:
    def kthSmallest(self, matrix: List[List[int]], k: int) -> int:
        matrixAsoneList = []
        for item in matrix: 
            matrixAsoneList.extend(item)
        matrixAsoneList.sort()
        return matrixAsoneList[k-1]