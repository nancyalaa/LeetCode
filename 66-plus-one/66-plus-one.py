class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        s = ""
        for i in digits:
            s += str(i)
        nums = int(s)
        nums = nums+1
        s2 = str(nums)
        L = []
        for i in s2:
            j = int(i)
            L.append(j)
        return L
        