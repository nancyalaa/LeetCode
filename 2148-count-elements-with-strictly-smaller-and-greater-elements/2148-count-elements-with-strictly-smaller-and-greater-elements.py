class Solution:
    def countElements(self, nums: List[int]) -> int:
        nums.sort()
        result = 0
        for num in nums:
            if num > min(nums) and num < max(nums):
                result += 1
        return result
        
            
        