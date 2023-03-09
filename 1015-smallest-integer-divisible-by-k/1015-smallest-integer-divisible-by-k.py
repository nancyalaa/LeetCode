class Solution:
    def smallestRepunitDivByK(self, k: int) -> int:
        remainder = 0
        for num in range(1, k+1):
            remainder = (remainder*10+1) % k
            if remainder == 0:
                return num
        return -1
        