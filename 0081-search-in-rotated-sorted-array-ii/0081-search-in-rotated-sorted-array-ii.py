class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        nums = set(nums)
        return target in nums
        