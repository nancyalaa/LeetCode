class Solution:
    def getRow(self, rowIndex: int) -> List[int]:
        rows = [[1], [1, 1]]
        if rowIndex > 1:
            for idx in range(rowIndex-1):
                temp = [1]
                for n in range(len(rows[idx+1])-1):
                    temp.append(rows[idx+1][n]+rows[idx+1][n+1])
                temp.append(1)
                rows.append(temp)
        return rows[rowIndex]
             
        
        