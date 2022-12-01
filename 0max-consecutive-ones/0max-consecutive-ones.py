class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        numberOfConsecutiveOnes = 0
        maxNumberOfConsecutiveOnes = 0
        for num in nums:
            if num == 1:
                numberOfConsecutiveOnes += 1
            else:
                if numberOfConsecutiveOnes > maxNumberOfConsecutiveOnes:
                    maxNumberOfConsecutiveOnes = numberOfConsecutiveOnes
                numberOfConsecutiveOnes = 0
        if numberOfConsecutiveOnes > maxNumberOfConsecutiveOnes:
            return numberOfConsecutiveOnes
        else:
            return maxNumberOfConsecutiveOnes
                
        