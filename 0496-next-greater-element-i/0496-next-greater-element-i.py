class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        output = []
        for num in nums1:
            flag = False
            if nums2.index(num) == len(nums2)-1: 
                flag = True
                output.append(-1)
            else:
                for n in nums2[nums2.index(num):]:
                    if n > num:
                        output.append(n)
                        flag = True
                        break
            if flag == False: output.append(-1) 
        return output