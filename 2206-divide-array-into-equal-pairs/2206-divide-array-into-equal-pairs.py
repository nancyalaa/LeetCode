class Solution:
    def divideArray(self, nums: List[int]) -> bool:
        nums_map = Counter(nums)
        for item in list(nums_map.values()):
            if item % 2 == 0: continue
            else: return False
        return True
        
        
        