class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        counter = 0
        for word in words:
            flag = False
            for char in set(word):
                if char in allowed:continue
                else:
                    flag = True
                    break
            if flag == False: counter += 1
        return counter
        