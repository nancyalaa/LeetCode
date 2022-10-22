class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        numberOfEven = 0
        for i in nums:
            cntr = 0
            while i > 0:
                i = i//10
                cntr += 1
            if cntr % 2 == 0:
                numberOfEven += 1
        return numberOfEven
                
                
        