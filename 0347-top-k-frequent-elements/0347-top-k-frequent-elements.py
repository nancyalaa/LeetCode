class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        freqs = Counter(nums)
        output = []
        for i in range(k):
            keyList = list(freqs.keys())
            valList = list(freqs.values())
            item = valList.index(max(valList))
            output.append(keyList[item])
            del freqs[keyList[item]]
        return output
                
            
        
        