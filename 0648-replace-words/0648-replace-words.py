class Solution:
    def replaceWords(self, dictionary: List[str], sentence: str) -> str:
        words = sentence.split(' ')
        for prefix in dictionary:
            for word in words:
                if word.find(prefix) == 0:
                    words[words.index(word)] = prefix
        return ' '.join(words)
        