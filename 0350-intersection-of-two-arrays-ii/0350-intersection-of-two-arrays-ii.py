class Solution:
    def intersect(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        if len(nums1) < len(nums2):
            for number in nums1:
                if number in nums2: 
                    output.append(number)
                    nums2.pop(nums2.index(number))
        else:
            for number in nums2:
                if number in nums1: 
                    output.append(number)
                    nums1.pop(nums1.index(number))
        return output
        
        