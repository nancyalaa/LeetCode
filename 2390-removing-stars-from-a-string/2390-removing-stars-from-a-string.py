class Solution:
    def removeStars(self, s: str) -> str:
        output = []
        for char in s:
            if char == '*':
                output.pop()
            else:
                output.append(char)
        return ''.join(output)
            
                