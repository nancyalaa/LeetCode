class Solution:
    def smallestEqual(self, nums: List[int]) -> int:
        output = []
        for i in range(len(nums)):
            if i % 10 == nums[i]:
                output.append(i)
        if len(output) > 0:
            return min(output)
        else:
            return -1
        