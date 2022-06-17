import re
class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        L = []
        for i in sentences:
            r = re.findall(r'\w+', i)
            L.append(len(r))
        return max(L)
            
        