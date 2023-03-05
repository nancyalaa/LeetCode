class Solution:
    def equalPairs(self, grid: List[List[int]]) -> int:
        output = 0
        for row in grid:
            for idx in range(len(grid[0])):
                column = []
                for col in range(len(grid)):
                    column.append(grid[col][idx])
                if column == row:
                    output += 1
        return output
                
                
        