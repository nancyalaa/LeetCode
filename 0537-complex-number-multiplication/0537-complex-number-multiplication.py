class Solution:
    def complexNumberMultiply(self, num1: str, num2: str) -> str:
        x, y = num1[:-1].split("+")
        u, v = num2[:-1].split("+")
        return str((int(x)*int(u)-int(y)*int(v)))+"+"+str((int(x)*int(v)+int(y)*int(u)))+"i"
        