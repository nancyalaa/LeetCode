class Solution:
    def mostCommonWord(self, paragraph: str, banned: List[str]) -> str:
        modified_paragraph = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])
        words = modified_paragraph.split(' ')
        while '' in words: words.pop(words.index(''))
        for idx in range(len(words)): 
            words[idx] = words[idx].lower()
        if len(banned) > 0:
            for word in banned:
                while word.lower() in words: words.pop(words.index(word))
        words_freq = Counter(words)
        values = list(words_freq.values())
        keys = list(words_freq.keys())
        return keys[values.index(max(values))]
        
        
        