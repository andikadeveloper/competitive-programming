from typing import List

class Solution:
    def minTimeToVisitAllPoints(self, points: List[List[int]]) -> int:
        x = 0
        
        for i in range(len(points) - 1):
            p = abs(points[i][0] - points[i+1][0])
            n = abs(points[i][1] - points[i+1][1])
            
            x += p if p > n else n
            
        return x

solution = Solution()
actual = solution.minTimeToVisitAllPoints([[1,1],[3,4],[-1,0]])
print(actual)
print(actual == 7)
