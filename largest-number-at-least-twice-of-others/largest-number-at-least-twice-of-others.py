class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        mx = max(nums)
        for i in nums:
            if i == mx:
                continue
            if i*2 <= mx:
                continue
            else:
                return -1
        return nums.index(mx)
            
                
        