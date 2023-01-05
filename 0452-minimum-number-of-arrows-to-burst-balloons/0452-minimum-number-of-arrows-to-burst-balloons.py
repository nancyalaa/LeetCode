class Solution:
    def findMinArrowShots(self, points: List[List[int]]) -> int:
        points.sort()
        previous = points[0]
        arrows = 1
        for start, end in points[1:]:
            if start > previous[1]:
                arrows += 1
                previous = [start, end]
            else:
                previous[1] = min(previous[1], end)
        return arrows
                
            
        