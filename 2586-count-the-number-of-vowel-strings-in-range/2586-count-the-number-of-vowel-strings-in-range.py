class Solution:
    def vowelStrings(self, words: List[str], left: int, right: int) -> int:
        output = 0
        for idx in range(left, right+1):
            if words[idx][0] in 'aeiou' and words[idx][-1] in 'aeiou': output += 1
        return output
        