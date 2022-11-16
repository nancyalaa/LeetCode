class Solution:
    def singleNonDuplicate(self, nums: List[int]) -> int:
        numsCount = Counter(nums)
        for num in numsCount:
            if numsCount[num] == 1:
                return num
        
        