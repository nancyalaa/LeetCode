class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        numberOfRows = len(mat)
        numberOfCols = len(mat[0])
        result = []
        currentRow = 0
        currentCol = 0
        toUp = True
        while len(result) != numberOfRows * numberOfCols:
            if toUp:
                while currentRow >= 0 and currentCol < numberOfCols:
                    result.append(mat[currentRow][currentCol])
                    currentRow -= 1
                    currentCol += 1
                if currentCol == numberOfCols:
                    currentCol -= 1
                    currentRow += 2
                else:
                    currentRow += 1
                toUp = False
            else:
                while currentRow < numberOfRows and currentCol >= 0:
                    result.append(mat[currentRow][currentCol])
                    currentRow += 1
                    currentCol -= 1
                if currentRow == numberOfRows:
                    currentRow -= 1
                    currentCol += 2
                else:
                    currentCol += 1
                toUp = True
        return result
                