class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        temp = []
        for num in nums:
            for char in str(num):
                temp.append(int(char))
        return abs(sum(temp)-sum(nums))
              
        