import numpy
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        nums = list(numpy.arange(1, arr[len(arr)-1]+k+1))
        for num in arr: 
            nums.pop(nums.index(num))
        return nums[k-1]
        