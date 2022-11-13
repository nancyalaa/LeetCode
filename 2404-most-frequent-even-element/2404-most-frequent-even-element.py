class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        temp = []
        for i in nums:
            if i % 2 == 0:
                temp.append(i)
        temp.sort()
        if len(temp) > 0:
            return max(temp, key=temp.count)
        else:
            return -1
    
        
        
        
        