class Solution:
    def findMaxK(self, nums: List[int]) -> int:
        while nums:
            mx = max(nums)
            if (mx * -1) in nums: return mx
            else: nums.pop(nums.index(mx))
        return -1