class Solution:
    def isCovered(self, ranges: List[List[int]], left: int, right: int) -> bool:
        output = 0
        for idx in range(left, right+1):
            for Range in ranges:
                if idx >= Range[0] and idx <= Range[1]: 
                    output += 1
                    break
        return output == right-left+1