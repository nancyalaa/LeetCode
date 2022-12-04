class Solution:
    def uniqueOccurrences(self, arr: List[int]) -> bool:
        arrMap = Counter(arr)
        occurences = list(arrMap.values())
        for i in occurences:
            if occurences.count(i) > 1:
                return False
        return True
        