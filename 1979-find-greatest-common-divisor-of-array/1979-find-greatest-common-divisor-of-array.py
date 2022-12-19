class Solution:
    def findGCD(self, nums: List[int]) -> int:
        mn = min(nums)
        mx = max(nums)
        for i in range(mx, 0, -1):
            if mx % i == 0 and mn % i == 0:
                return i
        return 1