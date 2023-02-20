class Solution:
    def findSpecialInteger(self, arr: List[int]) -> int:
        for num in set(arr):
            if arr.count(num) > (len(arr) * 25//100): return num