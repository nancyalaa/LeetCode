class Solution(object):
    def areOccurrencesEqual(self, s):
        """
        :type s: str
        :rtype: bool
        """
        temp = set(s)
        flag = 0
        for i in temp:
            if s.count(i) == s.count(s[0]):
                continue
            else:
                flag = 1
                break
        if flag:
            return False
        else:
            return True
        
        