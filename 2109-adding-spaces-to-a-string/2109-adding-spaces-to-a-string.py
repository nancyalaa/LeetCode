class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        output = []
        previous_split = 0
        for spaceIdx in spaces:
            output.append(s[previous_split:spaceIdx])
            previous_split = spaceIdx
        output.append(s[previous_split:])
        return ' '.join(output)
            
        