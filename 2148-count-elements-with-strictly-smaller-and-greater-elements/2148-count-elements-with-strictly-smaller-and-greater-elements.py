class Solution:
    def countElements(self, nums: List[int]) -> int:
        result = 0
        for num in set(nums):
            if num > min(nums) and num < max(nums):
                result += 1*nums.count(num)
        return result
        
            
        