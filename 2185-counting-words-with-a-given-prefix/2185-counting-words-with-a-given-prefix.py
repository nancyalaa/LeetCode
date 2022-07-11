class Solution:
    def prefixCount(self, words: List[str], pref: str) -> int:
        prefixLength = len(pref)
        numberOfWords = 0
        for i in words:
            if i[:prefixLength] == pref:
                numberOfWords += 1
        return numberOfWords
        