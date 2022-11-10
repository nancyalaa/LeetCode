class Solution(object):
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        allnums = list(range(1,len(nums)+1))
        return list(set(allnums).symmetric_difference(set(nums)))