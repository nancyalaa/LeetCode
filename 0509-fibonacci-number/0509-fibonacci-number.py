class Solution:
    def fib(self, n: int) -> int:
        sequence = [0, 1]
        for idx in range(2, n+1):
            sequence.append(sequence[idx-1]+sequence[idx-2])
        return sequence[n]
        