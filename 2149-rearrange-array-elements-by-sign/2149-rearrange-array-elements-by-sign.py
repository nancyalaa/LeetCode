class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        positives = []
        negatives = []
        for num in nums:
            if num == abs(num): positives.append(num)
            else: negatives.append(num)
        output = []
        for idx in range(len(positives)):
            output.append(positives[idx])
            output.append(negatives[idx])
        return output
        