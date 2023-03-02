class Solution:
    def arraySign(self, nums: List[int]) -> int:
        if prod(nums) > 0: return 1
        elif prod(nums) < 0: return -1
        else: return 0