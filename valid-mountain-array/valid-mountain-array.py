class Solution:
    def validMountainArray(self, arr: List[int]) -> bool:
        if len(arr) <= 2:
            return False
        if arr.index(max(arr)) == 0 or arr.index(max(arr)) == len(arr)-1:
            return False
    
        for i in range(arr.index(max(arr))):
            if arr[i] < arr[i+1]:
                continue
            else:
                return False
        j = len(arr)-1
        for i in range(len(arr)-arr.index(max(arr))):
            if j == arr.index(max(arr)):
                break
            if arr[j] < arr[j-1]:
                j -= 1
                continue
            else:
                return False
            
        return True
                       