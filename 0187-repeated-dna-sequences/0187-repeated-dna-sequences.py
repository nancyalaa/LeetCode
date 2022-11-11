class Solution:
    def findRepeatedDnaSequences(self, s: str) -> List[str]:
        dictt = collections.Counter()
        for i in range(len(s)-9):
            dictt[s[i:i+10]] += 1
        output = []
        for key in dictt:
            if dictt[key] > 1:
                output.append(key)
        return output
                        
            
            
            

            
        