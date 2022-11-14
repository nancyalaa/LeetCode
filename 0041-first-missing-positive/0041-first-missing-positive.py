class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        uniqueNums = set(nums)
        for i in range(1,len(nums)+2):
            if i not in uniqueNums: 
                return i
        