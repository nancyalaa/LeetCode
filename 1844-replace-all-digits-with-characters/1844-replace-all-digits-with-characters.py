class Solution:
    def replaceDigits(self, s: str) -> str:
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        output = ''
        for i in range(len(s)):
            if s[i] in alphabets:
                output += s[i]
            else:
                idx = alphabets.index(s[i-1])
                output += alphabets[int(s[i])+idx]
        return output