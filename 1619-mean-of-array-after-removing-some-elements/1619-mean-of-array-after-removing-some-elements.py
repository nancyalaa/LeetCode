class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort() 
        return sum(arr[5*len(arr)//100: len(arr)-5*len(arr)//100])/len(arr[5*len(arr)//100: len(arr)-5*len(arr)//100])
        
        