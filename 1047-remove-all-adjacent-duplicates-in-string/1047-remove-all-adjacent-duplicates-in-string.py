class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = [s[0]]
        for idx in range(1, len(s)):
            if stack and s[idx] == stack[len(stack)-1]: stack.pop(len(stack)-1)
            else: stack.append(s[idx])
        return "".join(stack)
            