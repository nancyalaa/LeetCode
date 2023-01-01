class Solution:
    def firstUniqChar(self, s: str) -> int:
        sMap = Counter(s)
        for key in sMap:
            if sMap[key] == 1:
                return s.index(key)
        return -1