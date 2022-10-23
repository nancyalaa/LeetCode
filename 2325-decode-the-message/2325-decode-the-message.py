class Solution(object):
    def decodeMessage(self, key, message):
        """
        :type key: str
        :type message: str
        :rtype: str
        """
        KEY = ""
        for i in key:
            if KEY.find(i) == -1 and i != ' ':
                KEY += i
       
        alphabets = "abcdefghijklmnopqrstuvwxyz"
        output = ''
        for i in message:
            if i == ' ':
                output += ' '
            else:
                for j in range(26):
                    if i == KEY[j]:
                        output += alphabets[j] 
        return output
            