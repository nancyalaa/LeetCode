class Solution:
    def trimMean(self, arr: List[int]) -> float:
        arr.sort() 
        number_of_elements_to_be_erased = 5*len(arr)//100
        return sum(arr[number_of_elements_to_be_erased: len(arr)-number_of_elements_to_be_erased])/len(arr[number_of_elements_to_be_erased: len(arr)-number_of_elements_to_be_erased])
        
        