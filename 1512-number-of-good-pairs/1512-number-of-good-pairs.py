class Solution:
    def numIdenticalPairs(self, nums: List[int]) -> int:
        cntr = 0 
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i] == nums[j] and i != j:
                    cntr += 1
        return cntr
        