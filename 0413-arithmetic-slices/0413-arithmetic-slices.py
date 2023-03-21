class Solution:
    def numberOfArithmeticSlices(self, nums: List[int]) -> int:
        number_of_subarrays, diffs = 0, 0
        for i in range(len(nums)-2):
            if nums[i] - nums[i+1] == nums[i+1] - nums[i+2]: diffs += 1
            else: diffs = 0
            number_of_subarrays += diffs
        return number_of_subarrays
        