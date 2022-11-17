class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        sumOfUniqueNums = 0
        numberFrequency = Counter(nums)
        for i in numberFrequency:
            if numberFrequency[i] == 1:
                sumOfUniqueNums += i
        return sumOfUniqueNums
                
            
        