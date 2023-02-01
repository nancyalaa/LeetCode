class compare_nums(str):
    def __lt__(str1, str2):
        return str1+str2 > str2+str1
        
class Solution:
    def largestNumber(self, nums):
        largest_num = ''.join(sorted(map(str, nums), key=compare_nums))
        return '0' if largest_num[0] == '0' else largest_num
        
        