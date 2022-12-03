class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = 'aeiou'
        temp = ''
        for i in s:
            if i.lower() in vowels:
                temp += i
        temp = temp[::-1]
        output = ''
        j = 0
        for i in s:
            if i.lower() not in vowels:
                output += i
            else:
                output += temp[j]
                j += 1
        return output
                
        