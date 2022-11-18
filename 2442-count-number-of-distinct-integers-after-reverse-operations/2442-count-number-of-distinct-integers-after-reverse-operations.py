class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        result = nums
        for num in set(nums):
            numToStr = str(num)
            numToStr = numToStr[::-1]
            result.append(int(numToStr))
        return len(set(result))
            
        