class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        numsCount = Counter(nums)
        output = []
        for num in numsCount:
            if numsCount[num] == 1 and numsCount[num-1] == 0 and numsCount[num+1] == 0:
                output.append(num)
        return output
        