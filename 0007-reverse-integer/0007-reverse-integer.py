class Solution:
    def reverse(self, x: int) -> int:
        if x >= 2**31-1 or x <= -2**31: 
            return 0
        temp = x
        flag = False
        if x < 0 :
            x = abs(x)
            flag = True
        output = 0
        while(x > 0):
            lastDigit = x % 10
            x = x // 10
            output = output * 10 + lastDigit
        
        if output >= 2**31-1 or output <= -2**31: 
                return 0
        else:
            if flag:
                return -1*output
            else:
                return output
         
        
        