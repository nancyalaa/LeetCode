class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        nums1, nums2 = set(nums1), set(nums2)
        nums1_and_nums2_intersection = list(nums1.intersection(nums2))
        return -1 if len(nums1_and_nums2_intersection) == 0 else min(nums1_and_nums2_intersection)
            
        
        
        