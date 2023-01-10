class Solution:
    def maximumCount(self, nums: List[int]) -> int:
        positive_count = 0
        negative_count = 0
        for num in nums:
            if num>0: positive_count += 1
            if num<0: negative_count += 1
        return max(positive_count, negative_count)