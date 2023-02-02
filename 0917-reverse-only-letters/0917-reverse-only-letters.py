class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        special_chars = []
        special_chars_indecies = []
        reversed_str = []
        for idx in range(len(s)):
            if s[idx].isalpha() == False:
                special_chars.append(s[idx])
                special_chars_indecies.append(idx)
            else: reversed_str.append(s[idx])
        reversed_str.reverse()
        ctr = 0
        for idx in range(len(s)):
            if idx in special_chars_indecies:
                reversed_str.insert(idx, special_chars[ctr])
                ctr += 1
        return "".join(reversed_str)
        
            
        