class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        stringsMap = {}
        for string in strs:
            sortedString = ''.join(sorted(string))
            if sortedString not in stringsMap:
                stringsMap[sortedString] = []
            stringsMap[sortedString].append(string)
        return stringsMap.values()
                
                
                
        