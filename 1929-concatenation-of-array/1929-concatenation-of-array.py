class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        L = []
        for i in nums:
            L.append(i)
        for i in nums:
            L.append(i)
        return L
        