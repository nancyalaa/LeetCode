class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        left, right, count = {}, {}, {}
        for i, j in enumerate(nums):
            if j not in left: left[j] = i
            right[j] = i
            count[j] = count.get(j, 0) + 1

        answer = len(nums)
        degree = max(count.values())
        for j in count:
            if count[j] == degree:
                answer = min(answer, right[j] - left[j] + 1)

        return answer