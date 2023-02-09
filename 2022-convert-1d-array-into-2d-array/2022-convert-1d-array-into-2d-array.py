class Solution:
    def construct2DArray(self, original: List[int], m: int, n: int) -> List[List[int]]:
        if n*m != len(original): return  []
        output = []
        idx = 0
        for row in range(m):
            temp = []
            for col in range(n):
                temp.append(original[idx])
                idx += 1
            output.append(temp)
        return output
        