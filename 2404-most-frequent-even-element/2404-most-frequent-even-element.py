class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        flag = False
        freqs = collections.Counter()
        for i in nums:
            if i % 2 == 0:
                flag = True
                freqs[i] += nums.count(i)
        if flag:
            mx = max(freqs.values())
            output = []
            for key in freqs:
                if freqs[key] == mx:
                    output.append(key)
            return min(output)
        
        else:
             return -1
        
        