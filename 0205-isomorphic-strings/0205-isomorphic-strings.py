class Solution:
    def isIsomorphic(self, s: str, t: str) -> bool:
        sMapt = {}
        tMaps = {} 
        for i in range(len(s)):
            if s[i] not in sMapt.keys():
                sMapt[s[i]] = t[i]
            else:
                if sMapt[s[i]] == t[i]:
                    continue
                else:
                    return False
            if t[i] not in tMaps.keys():
                tMaps[t[i]] = s[i]
            else:
                if tMaps[t[i]] == s[i]:
                    continue
                else:
                    return False
        return True
                
        