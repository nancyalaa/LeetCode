class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        number_of_subarrays, zeros = 0, 0
        for num in nums:
            if num == 0: zeros += 1
            else: zeros = 0
            number_of_subarrays += zeros
        return number_of_subarrays
                
        