class Solution:
    def jump(self, nums: List[int]) -> int:
        jump = farthest = currEnd = 0
        
        for idx in range(len(nums) - 1):
            farthest = max(farthest, idx + nums[idx])
            if idx == currEnd:
                jump += 1
                currEnd = farthest
                if currEnd >= len(nums) - 1:
                    return jump
        return jump