class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        numsSet = set(nums)
        longestConsSeq = 0
        for num in numsSet:
            if num-1 not in numsSet:
                seqLen = 1
                while num+seqLen in numsSet:
                    seqLen += 1
                longestConsSeq = max(longestConsSeq, seqLen)
        return longestConsSeq
                
            
       
       
            
        
        