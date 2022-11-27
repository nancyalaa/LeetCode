class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        sumOfDigits = 0
        power = len(digits)-1
        for i in digits:
            sumOfDigits += ((10**power) * i)
            power -= 1
        sumOfDigits += 1
        result = []
        while(sumOfDigits > 0):
            result.append(sumOfDigits % 10)
            sumOfDigits //= 10
        result.reverse()
        return result
        