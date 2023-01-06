class Solution:
    def maxIceCream(self, costs: List[int], coins: int) -> int:
        costs.sort()
        if costs[0] > coins: return 0
        totalCost = costs[0]
        numberOficeCream = 1
        for cost in range(1, len(costs)):
            if totalCost+costs[cost] <= coins:
                totalCost += costs[cost]
                numberOficeCream += 1
            else: break
        return numberOficeCream