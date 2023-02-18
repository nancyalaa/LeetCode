class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        output = ""
        for char in set(t):
            if t.count(char) != s.count(char): output += char*(t.count(char)-s.count(char))
        return output
