class Solution:
    def triangularSum(self, nums: List[int]) -> int:
        ln = len(nums)
        while ln > 0:
            for i in range(ln-1):
                nums[i] = (nums[i] + nums[i+1]) % 10
            ln -= 1
        return nums[0]
            
        