class Solution:
    def customSortString(self, order: str, s: str) -> str:
        output = ""
        for i in order:
            for j in s:
                if j == i:
                    output += j
                    
                    
        rest = ""
        for i in s:
            if i not in output:
                rest += i
        return output + rest
        