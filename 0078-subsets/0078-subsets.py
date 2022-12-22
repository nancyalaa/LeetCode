class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        return [list(subset) for item in range(len(nums)+1) for subset in itertools.combinations(nums, item)]
        