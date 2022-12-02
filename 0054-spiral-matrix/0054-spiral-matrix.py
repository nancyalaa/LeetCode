class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result = []
        if len(matrix) == 1:
            return matrix[0]
        if len(matrix[0]) == 1:
            for i in matrix:
                result.extend(i)
            return result
        while len(matrix) > 0:
            
            #right
            result.extend(matrix[0])
            matrix.pop(0)
            
            #down
            for i in range(len(matrix)):
                if len(matrix) > 0  and len(matrix[0]) > 0:
                    result.append(matrix[i][len(matrix[i])-1])
                    matrix[i].pop(len(matrix[i])-1)
              
                
            #left
            if len(matrix)>0:
                temp = matrix[len(matrix)-1]
                temp.reverse()
                result.extend(temp)
                matrix.pop(len(matrix)-1)
            
            #up
            i = len(matrix)-1
            for j in range(len(matrix)):
                if len(matrix) > 0 and len(matrix[0]) > 0:
                    result.append(matrix[i][0])
                    matrix[i].pop(0)
                i -= 1
            
        return result
            
                
            
        
        
    
                
        