class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        numberOfCols = 0
        for col in range(len(strs[0])):
            for row in range(1,len(strs)):
                if strs[row][col] < strs[row-1][col]:
                    numberOfCols += 1
                    break
        return numberOfCols
        
            
                