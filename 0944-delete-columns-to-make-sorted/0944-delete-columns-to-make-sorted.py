class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        output = 0
        for row in zip(*strs):
            if list(row)!=sorted(row):
                output+=1
        return output 
        
            
                