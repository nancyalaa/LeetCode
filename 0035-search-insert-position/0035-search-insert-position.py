class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int: 
        if target > max(nums):
            return len(nums)
        if target < min(nums):
            return 0
        for i in range(len(nums)):
                if nums[i] >= target:
                    return i
                
        