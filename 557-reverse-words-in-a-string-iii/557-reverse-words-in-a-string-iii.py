class Solution:
    def reverseWords(self, s: str) -> str:
        ListOfWords = s.split()
        NewString = ""
        for i in range(0, len(ListOfWords)):
            NewString += ListOfWords[i][::-1]
            if i != len(ListOfWords) -1:
                NewString += " "
        return NewString
        