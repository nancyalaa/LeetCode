class Solution:
    def addDigits(self, num: int) -> int:
        while len(str(num)) != 1:
            summ = 0
            for char in str(num):
                summ += int(char)
            num = summ
        return num
            