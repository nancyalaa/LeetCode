class Solution:
    def reversePrefix(self, word: str, ch: str) -> str:
        if word.find(ch) == -1:
            return word
        idx = word.index(ch)
        if idx == len(word)-1:
            return word[::-1]
        return word[:idx+1][::-1] + word[idx+1:]