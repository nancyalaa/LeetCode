class Solution:
    def findMiddleIndex(self, nums: List[int]) -> int:
        rightSum = 0
        leftSum = 0
        for i in range(len(nums)):
            rightSum = sum(nums[i+1:])
            if rightSum == leftSum:
                return i
            else:
                leftSum += nums[i]
        return -1
        
        