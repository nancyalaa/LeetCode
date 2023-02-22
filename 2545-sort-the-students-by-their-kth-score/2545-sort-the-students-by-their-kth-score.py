class Solution:
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        k_scores_indecies = []
        i = 0
        for row in score:
            k_scores_indecies.append([row[k], i])
            i += 1
        k_scores_indecies.sort(reverse=True)
        output = []
        for item in k_scores_indecies:
            output.append(score[item[1]])
        return output
            
             
                
                
        