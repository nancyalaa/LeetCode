class Solution:
    def sortPeople(self, names: List[str], heights: List[int]) -> List[str]:
        names_and_heights = []
        for idx in range(len(heights)):
            names_and_heights.append([heights[idx], names[idx]])
        names_and_heights.sort(reverse=True)
        output = []
        for item in names_and_heights:
            output.append(item[1])
        return output
        
            