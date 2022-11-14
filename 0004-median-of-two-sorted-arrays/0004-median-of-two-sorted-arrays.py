class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        merged = nums1 + nums2
        merged.sort()
        if len(merged) % 2 != 0:
            return merged[len(merged)//2] 
        else:
            return (merged[(len(merged)//2)] + merged[(len(merged)//2)-1]) / 2 
        