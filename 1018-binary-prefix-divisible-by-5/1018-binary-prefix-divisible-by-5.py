class Solution:
    def prefixesDivBy5(self, nums: List[int]) -> List[bool]:
        output = [] 
        prefix = ''
        for i in nums:
            prefix += str(i)
            output.append(int(prefix,2)%5==0)
        return output
       
        