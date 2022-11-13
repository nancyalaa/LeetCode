class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        output = []
        temp = set(nums)
        for i in temp:
            if nums.count(i) > len(nums)//3:
                output.append(i)
        return output
        