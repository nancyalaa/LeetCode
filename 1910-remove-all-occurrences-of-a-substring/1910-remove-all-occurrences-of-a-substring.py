class Solution:
    def removeOccurrences(self, s: str, part: str) -> str:
            while 1:
                if s.find(part) == -1:
                    return s
                    break
                else:
                    s = s.replace(part,'',1)
             