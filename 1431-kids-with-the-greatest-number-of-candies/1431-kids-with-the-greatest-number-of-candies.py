class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        result = []
        for i in range(len(candies)):
            result.append(0)
        c = 0
        for i in candies:
            if i + extraCandies >= max(candies):
                result[c] = True
            else:
                result[c] = False
            c += 1
        return result
                
            
        