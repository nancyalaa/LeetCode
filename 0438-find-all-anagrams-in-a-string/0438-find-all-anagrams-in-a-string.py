class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        output = []
        p = "".join(sorted(p))
        for idx in range(0, len(s)-len(p)+1):
            if ''.join(sorted(s[idx: idx+len(p)])) == p: output.append(idx)
        return output
        