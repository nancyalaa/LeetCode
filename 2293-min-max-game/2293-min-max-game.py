class Solution:
    def minMaxGame(self, nums: List[int]) -> int: 
        while len(nums) != 1:
            temp = []
            mn = True
            for i in range(0, len(nums), 2):
                if mn:
                    temp.append(min(nums[i: i+2]))
                    mn = False
                else: 
                    temp.append(max(nums[i: i+2]))
                    mn = True    
            nums[:] = temp
        return nums[0]
                
                
        
        