class Solution:
    def findMin(self, nums: List[int]) -> int:
        nums = set(nums)
        return min(nums)
        