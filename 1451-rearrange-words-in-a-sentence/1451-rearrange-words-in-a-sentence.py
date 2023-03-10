class Solution:
    def arrangeWords(self, text: str) -> str:
        text = text.split(' ')
        text.sort(key=len)
        output = text[0].title()
        for idx in range(1, len(text)):
            output += " "+text[idx].lower()
        return output
        
        
        