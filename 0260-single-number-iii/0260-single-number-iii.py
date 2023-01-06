class Solution:
    def singleNumber(self, nums: List[int]) -> List[int]:
        output = []
        nums = Counter(nums)
        for key in nums:
            if nums[key] == 1: output.append(key)
        return output
        