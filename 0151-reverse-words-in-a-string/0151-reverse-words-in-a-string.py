class Solution:
    def reverseWords(self, s: str) -> str:
        listOfWords = s.split(' ')
        listOfWords.reverse()
        return re.sub(' +', ' ', ' '.join(listOfWords).strip())