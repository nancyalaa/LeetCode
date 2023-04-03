class Solution:
    def isPossibleDivide(self, nums: List[int], k: int) -> bool:
        if len(nums)%k != 0: return False
        nums_map = Counter(nums)
        while nums_map:
            start = min(nums_map.keys())
            print(start)
            for idx in range(start, start+k):
                if idx in nums_map:
                    nums_map[idx] -= 1
                    if nums_map[idx] == 0: nums_map.pop(idx)
                else: return False
        return True
            