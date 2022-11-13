class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        freqs = Counter(nums)
        output = []
        for i in freqs:
            if freqs[i] > len(nums)//3:
                output.append(i)
        return output
            
        
        