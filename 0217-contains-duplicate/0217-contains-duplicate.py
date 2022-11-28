class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        uniqueNums = Counter(nums)
        if max(uniqueNums.values()) > 1:
            return True
        return False
        