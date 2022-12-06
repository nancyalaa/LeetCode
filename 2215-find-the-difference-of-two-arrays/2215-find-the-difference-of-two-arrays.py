class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        output = []
        temp1 = []
        temp2 = []
        for i in nums1:
            if i not in nums2 and i not in temp1:
                temp1.append(i)
        for i in nums2:
            if i not in nums1 and i not in temp2:
                temp2.append(i)
        output.append(temp1)
        output.append(temp2)
        return output
        