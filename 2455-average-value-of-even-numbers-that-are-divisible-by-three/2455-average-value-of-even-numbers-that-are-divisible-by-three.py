class Solution:
    def averageValue(self, nums: List[int]) -> int:
        cntr = 0
        evenSum = 0
        for i in nums:
            if i % 2 == 0 and i % 3 == 0:
                evenSum += i
                cntr += 1
        if cntr: return evenSum // cntr
        else: return 0