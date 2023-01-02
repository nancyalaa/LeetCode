class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        if word == word.upper():
            return True
        elif word == word.lower():
            return True
        elif word == word[0].upper() + word[1:].lower():
            return True
        return False
        