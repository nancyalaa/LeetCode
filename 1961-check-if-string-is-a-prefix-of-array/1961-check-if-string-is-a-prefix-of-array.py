class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        word = ''.join(words)
        if word.find(s) == 0:
            output = ''
            for word in words:
                output += word
                if output == s: return True
        return False
        