class Solution:
    def generate(self, numRows: int) -> List[List[int]]:
        if numRows == 1:
            return [[1]]
        if numRows == 2:
            return [[1],[1,1]]
        output = [[1],[1,1]]
        for i in range(2,numRows):
            temp = [1]
            for itm in range(len(output[i-1])-1):
                temp.append(output[i-1][itm]+output[i-1][itm+1])
            temp.append(1)
            output.append(temp)
        return output
       
                
            
        