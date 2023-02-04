class Solution:
    def maxProduct(self, words: List[str]) -> int:
        output = 0
        words = list(set(words))
        for i in range(len(words)):
            for j in range(i+1, len(words)):
                flag = False
                for char in set(words[i]):
                    if char in set(words[j]):
                        flag = True
                        break
                if flag == False: output = max(output, len(words[i])*len(words[j]))
        return output
        