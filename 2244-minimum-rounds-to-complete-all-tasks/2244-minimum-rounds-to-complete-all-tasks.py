class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        minimumRounds = 0
        numsFrequencies = Counter(tasks)
        for count in numsFrequencies.values():
            if count == 1: return -1
            elif count % 3 == 0: minimumRounds += count//3
            else: minimumRounds += count//3 + 1
        return minimumRounds
        