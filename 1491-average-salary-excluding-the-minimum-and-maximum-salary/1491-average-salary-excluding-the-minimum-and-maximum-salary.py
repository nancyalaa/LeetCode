class Solution:
    def average(self, salary: List[int]) -> float:
        salary.pop(salary.index(max(salary)))
        salary.pop(salary.index(min(salary)))
        return sum(salary)/len(salary)