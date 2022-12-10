class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        words = s.split()
        if len(pattern) != len(words):
            return False
        Map = {}
        for i in range(len(pattern)):
            if pattern[i] not in Map.keys():
                if words[i] not in Map.values():
                    Map[pattern[i]] = words[i]
                else:
                    return False
            if Map[pattern[i]] == words[i]:
                continue
            else:
                return False
        return True
        