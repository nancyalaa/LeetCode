class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        output = []
        if target in nums:
            output.append(nums.index(target))
        else:
            return [-1, -1]
        idx = len(nums) - 1 
        for num in range(len(nums)):
            if nums[idx] == target:
                output.append(idx)
                return output
            idx -= 1
            
         
        