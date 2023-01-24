class Solution:
    def maximumGap(self, nums: List[int]) -> int:
        nums = Counter(nums)
        nums = list(nums.keys())
        if len(nums) < 2: return 0
        nums.sort()
        differences = []
        for idx in range(1, len(nums)):
            differences.append(nums[idx]-nums[idx-1])
        return max(differences)
        
            
        