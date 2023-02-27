class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        output = []
        for idx in range(len(nums)):
            temp = nums[idx+1:] + nums[:idx]
            flag = False
            for n in temp:
                if n > nums[idx]:
                    output.append(n)
                    flag = True
                    break
            if flag == False: output.append(-1)
        return output
        
        