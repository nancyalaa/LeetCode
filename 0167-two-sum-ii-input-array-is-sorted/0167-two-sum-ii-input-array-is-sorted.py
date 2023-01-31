class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        numbers_map = {}
        for idx, number in enumerate(numbers):
            if target-number in numbers_map.keys():
                return [numbers_map[target-number]+1, idx+1]
            numbers_map[number] = idx
            
        