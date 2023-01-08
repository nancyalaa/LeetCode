class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        if len(points) < 3 : return len(points)
        count = 1
        for i in range(0,len(points)):
            dict_slope = {}  
            for j in range(i+1,len(points)):
                if points[j][0] - points[i][0] == 0:
                     slope = 'INF'
                else:
                    slope = (points[j][1] - points[i][1]) / (points[j][0] - points[i][0]) 
                if slope in dict_slope:
                    dict_slope[slope] += 1
                else:
                    dict_slope[slope] = 1
            for i in dict_slope:
                count = max(count,dict_slope[i]+1) 
        return count
        