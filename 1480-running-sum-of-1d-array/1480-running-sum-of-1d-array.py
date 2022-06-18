class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        L = []
        L.append(nums[0])
        for i in range(1, len(nums)):
            L.append(L[i-1]+nums[i])
        return L