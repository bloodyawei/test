class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        count = 0
        point1 = points[0]
        for i in range(1, len(points)):
            point2 = points[i]
            dx, dy = point2[0]-point1[0], point2[1]-point1[1]
            count += max(abs(dx), abs(dy))
            point1 = point2
        return count
