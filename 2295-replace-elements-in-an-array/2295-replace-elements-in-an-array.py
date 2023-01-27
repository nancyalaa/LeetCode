class Solution:
    def arrayChange(self, nums: List[int], operations: List[List[int]]) -> List[int]:
        nums_map = {} 
        for idx, num in enumerate(nums):
            nums_map[num] = idx 
        for operation in operations:
            item_idx = nums_map[operation[0]] 
            nums[item_idx] = operation[1] 
            del nums_map[operation[0]]  
            nums_map[operation[1]] = item_idx 
            
        return nums
        
        