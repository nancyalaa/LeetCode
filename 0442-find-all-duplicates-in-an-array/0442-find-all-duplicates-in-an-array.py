class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        output = []
        numbers = collections.Counter()
        for i in nums:
            numbers[i] += 1
        for key in numbers:
            if numbers[key] == 2:
                output.append(key)
        return output