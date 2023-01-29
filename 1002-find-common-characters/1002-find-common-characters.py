class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        output = []
        for char in words[0]:
            is_found = True
            for idx in range(1, len(words)):
                if char in words[idx]: words[idx] = words[idx].replace(char, '', 1)
                else: is_found = False
            if is_found == True: output.append(char)
        return output
        