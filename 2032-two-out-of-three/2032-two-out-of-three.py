class Solution:
    def twoOutOfThree(self, nums1: List[int], nums2: List[int], nums3: List[int]) -> List[int]:
        all_nums = nums1 + nums2 + nums3
        output = []
        for num in set(all_nums):
            if num in nums1:
                if num in nums2 or num in nums3 and num not in output: output.append(num)
            elif num in nums2:
                if num in nums1 or num in nums3 and num not in output: output.append(num)
            elif num in nums3:
                if num in nums1 or num in nums2 and num not in output: output.append(num)
        return output