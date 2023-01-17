class Solution:
    def maximumValue(self, strs: List[str]) -> int:
        output = []
        for string in strs:
            if string.isnumeric() == True: output.append(int(string))
            else: output.append(len(string))
        return max(output)        
        