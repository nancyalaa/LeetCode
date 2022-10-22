class Solution:
    def truncateSentence(self, s: str, k: int) -> str:
        res = s.split(' ')
        return ' '.join(res[:k])
