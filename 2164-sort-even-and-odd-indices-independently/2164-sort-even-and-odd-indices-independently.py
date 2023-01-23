class Solution:
    def sortEvenOdd(self, nums: List[int]) -> List[int]:
        evens = []
        odds = []
        for idx in range(len(nums)):
            if idx % 2 == 0: evens.append(nums[idx])
            else: odds.append(nums[idx])
        evens.sort()
        odds.sort()
        odds.reverse()
        evensIdx = 0
        oddsIdx = 0
        output = []
        for idx in range(len(nums)):
            if idx % 2 == 0: 
                output.append(evens[evensIdx])
                evensIdx += 1
            else:
                output.append(odds[oddsIdx])
                oddsIdx += 1
        return output
                
            