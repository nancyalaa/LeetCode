class Solution:
    def secondHighest(self, s: str) -> int:
        digits = []
        for char in s:
            if char.isdigit() == True:
                digits.append(int(char))
        digits = list(set(digits))
        if len(digits) > 1:
            digits.sort()
            digits.remove(max(digits))
            return digits[len(digits)-1]
        return -1
        