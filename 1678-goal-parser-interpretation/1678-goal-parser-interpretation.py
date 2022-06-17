class Solution:
    def interpret(self, command: str) -> str:
        s = ''
        command = command.replace('()', 'o')
        for i in command:
            if i == '(' or i ==')':
                continue
            else:
                s += i
        return s
   
        