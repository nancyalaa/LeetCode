class Solution:
    def deleteGreatestValue(self, grid: List[List[int]]) -> int:
        output = 0
        while(grid[0]):
            temp = []
            for row in range(len(grid)):
                temp.append(grid[row].pop(grid[row].index(max(grid[row]))))
            output += max(temp)  
        return output
                
            
                
        