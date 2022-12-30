class Solution:
    def frequencySort(self, s: str) -> str:
        sFreqs = Counter(s)
        chars = list(sFreqs.keys())
        charFreqs = list(sFreqs.values())
        output = ""
        while charFreqs:
            output += chars[(charFreqs.index(max(charFreqs)))]*max(charFreqs)
            charFreqs.pop(charFreqs.index(max(charFreqs)))
            chars.pop(chars.index(output[len(output)-1]))
        return output