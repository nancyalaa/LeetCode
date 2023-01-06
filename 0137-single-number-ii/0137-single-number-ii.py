class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        nums = Counter(nums)
        for key in nums:
            if nums[key] == 1: return key