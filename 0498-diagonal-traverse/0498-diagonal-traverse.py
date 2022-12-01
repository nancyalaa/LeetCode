class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        if len(mat) == 0:
            return []
        if len(mat[0]) == 1:
            result = []
            for i in mat:
                result.extend(i)
            return result
        if len(mat) == 1:
            result = []
            for i in mat[0]:
                result.append(i)
            return result
        result = []
        for k in range(len(mat)+len(mat[0])):
            temp = []
            for i in range(len(mat)):
                for j in range(len(mat[0])):
                    if i + j == k:
                        temp.append(mat[i][j])
            if k % 2 == 0:
                temp.reverse()
            result.extend(temp)
                        
        return result