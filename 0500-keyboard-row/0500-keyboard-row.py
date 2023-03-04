class Solution:
    def findWords(self, words: List[str]) -> List[str]:
        rows = ["qwertyuiop", "asdfghjkl", "zxcvbnm"]
        output = []
        for word in words:
            for row in rows:
                flag = True
                for char in set(word):
                    if char.lower() in row: continue
                    else: 
                        flag = False
                        break
                if flag == True: 
                    output.append(word)
                    break
        return output
                    
                    
        