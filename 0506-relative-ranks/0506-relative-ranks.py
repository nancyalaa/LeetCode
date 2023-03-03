class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:
        temp = score.copy()
        temp.sort(reverse=True)
        output = []
        for num in score:
            if temp.index(num) == 0: output.append("Gold Medal")
            elif temp.index(num) == 1: output.append("Silver Medal")
            elif temp.index(num) == 2: output.append("Bronze Medal")
            else: output.append(str(temp.index(num)+1))
        return output
        