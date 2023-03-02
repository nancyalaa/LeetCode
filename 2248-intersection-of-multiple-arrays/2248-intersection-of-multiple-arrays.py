class Solution:
    def intersection(self, nums: List[List[int]]) -> List[int]:
        output = list(reduce(set.intersection, [set(item) for item in nums ]))
        output.sort()
        return output
        