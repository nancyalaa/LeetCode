class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsMap = Counter(nums)
        mx = 0
        for num in numsMap.keys():
            if num-1 not in numsMap.keys():
                seqLen = 1
                while num+seqLen in numsMap.keys():
                    seqLen += 1
                mx = max(mx,seqLen)
        return mx
            
       
       
            
        
        