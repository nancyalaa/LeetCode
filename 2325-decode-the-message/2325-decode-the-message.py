class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        modifiedKey = ""
        for i in key:
            if i not in modifiedKey and i != ' ':
                modifiedKey += i
        Map = {}
        for i in range(26):
            Map[modifiedKey[i]] = alphabets[i]
        output = ""
        for i in message:
            if i == ' ':
                output += ' '
            else:
                output += Map[i]
        return output
            
        
            
        
            
            