class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if len(strs) == 1:
            return strs[0]
        minLen = len(strs[0])
        for i in strs:
            if len(i) < minLen:
                minLen = len(i)
        if minLen == 0:
            return ''
        res = ''
        flag = True
        for i in range(minLen):
            pref = strs[0][i]
            print(pref)
            for string in strs:
                if string[i] == pref:
                    continue
                else:
                    flag = False
            if flag:
                res += pref
            else:
                return res
        return res
                
            
        