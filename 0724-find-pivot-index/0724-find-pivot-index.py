class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        
        leftSum = 0
        for i in range(len(nums)):
            if leftSum == sum(nums[i+1:]):
                return i
            leftSum += nums[i]
        return -1
            
           
            
            
                
            
            
        