class Solution:
    def findDuplicate(self, nums: List[int]) -> int:
        uniqueNums = set()
        for i in nums:
            if i not in uniqueNums:
                uniqueNums.add(i)
            else:
                return i
                
        
        