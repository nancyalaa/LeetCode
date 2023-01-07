class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        if sum(gas) < sum(cost):
            return -1
        tank = 0
        start = 0
        for station in range(len(gas)):
            tank += gas[station] - cost[station]
            if tank < 0:
                start = station + 1
                tank = 0 
        return start
        