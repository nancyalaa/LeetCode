class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        s = 0
        for i in operations:
            if i.count('+')>0 :
                s += 1
            else:
                s -= 1
        return s
        