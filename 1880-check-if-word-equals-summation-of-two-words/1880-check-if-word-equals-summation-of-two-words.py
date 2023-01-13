class Solution:
    def isSumEqual(self, firstWord: str, secondWord: str, targetWord: str) -> bool:
        alphabets = 'abcdefghijklmnopqrstuvwxyz'
        targetWord_sum = ''
        for char in targetWord:
            targetWord_sum += str(alphabets.index(char))
        firstWord_sum = ''
        for char in firstWord:
            firstWord_sum += str(alphabets.index(char))
        secondWord_sum = ''
        for char in secondWord:
            secondWord_sum += str(alphabets.index(char))
            
        return int(firstWord_sum) + int(secondWord_sum) == int(targetWord_sum)
        
        