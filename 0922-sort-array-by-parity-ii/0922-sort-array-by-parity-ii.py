class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        evens = []
        odds = []
        for num in nums:
            if num%2 == 0: evens.append(num)
            else: odds.append(num)
        output = []
        for idx in range(len(evens)):
            output.append(evens[idx])
            output.append(odds[idx])
        return output
        