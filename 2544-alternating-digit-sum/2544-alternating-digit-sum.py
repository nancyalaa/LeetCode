class Solution:
    def alternateDigitSum(self, n: int) -> int:
        num = str(n)
        num = num[::-1]
        n = int(num)
        output = 0
        i = 0
        while n > 0:
            if i % 2 == 0: output += n%10
            else: output -= n%10
            n = n//10
            i += 1
        return output
                
        