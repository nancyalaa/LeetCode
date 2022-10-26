class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        flag = 0
        for i in s:
            if s.count(i) == s.count(s[0]):
                continue
            else:
                flag = 1
                break
            
        if flag == 1:
            return False
        else:
            return True
        
        