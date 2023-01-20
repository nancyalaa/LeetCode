class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        subarrays = []
        for i in range(len(arr)):
            for j in range(len(arr)):
                if j>=i:
                    subarrays.append([*arr[i:j+1]])
        result = 0
        for subarray in subarrays:
            if len(subarray) % 2 != 0: result += sum(subarray)
        return result
         