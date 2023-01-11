class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        answer = []
        for num in set(nums):
            if nums.count(num) <= 2:
                answer.extend([num]*nums.count(num))
            else: 
                answer.extend([num]*2)
        answer.sort()
        nums[:] = answer
                
        
        