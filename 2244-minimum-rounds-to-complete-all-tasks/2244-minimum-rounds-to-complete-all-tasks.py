class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        minimumRounds = 0
        numsFrequencies = Counter(tasks)
        if 1 in numsFrequencies.values(): return -1
        for key in numsFrequencies.keys():
            if numsFrequencies[key] % 3 == 0: minimumRounds += numsFrequencies[key] // 3
            else: minimumRounds += numsFrequencies[key] // 3 + 1
        return minimumRounds
                
        