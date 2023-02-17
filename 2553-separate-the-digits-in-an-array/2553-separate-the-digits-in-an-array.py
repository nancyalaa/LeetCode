class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        digits = ''
        for num in nums:
            digits += str(num)
        output = []
        for digit in digits:
            output.append(int(digit))
        return output
        
        