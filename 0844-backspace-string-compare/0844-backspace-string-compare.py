class Solution:
    def backspaceCompare(self, s: str, t: str) -> bool:
        s_output = []
        t_output = []
        for s_char in s:
            if s_char == '#': 
                if len(s_output) > 0: s_output.pop()
            else: s_output.append(s_char)
        for t_char in t:
            if t_char == '#': 
                if len(t_output) > 0: t_output.pop()
            else: t_output.append(t_char)
        return s_output == t_output
        