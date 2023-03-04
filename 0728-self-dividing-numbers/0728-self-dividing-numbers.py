class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> List[int]:
        output = []
        for num in range(left, right+1):
            if num <= 9: output.append(num)
            else:
                flag = True
                num_chars = str(num)
                if '0' in num_chars: continue
                else:
                    for char in num_chars:
                        if num % int(char) == 0: continue
                        else:
                            flag = False
                            break
                    if flag == True: output.append(num)
        return output
                     
        