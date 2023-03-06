import numpy
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        nums = list(numpy.arange(1, 100000))
        for num in arr: 
            nums.pop(nums.index(num))
        return nums[k-1]
        