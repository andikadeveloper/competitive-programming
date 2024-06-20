from typing import List

class Solution:
    def garbageCollection(self, garbage: List[str], travel: List[int]) -> int:
        x = 0
        m = 0
        p = 0
        g = 0
        
        for i in range(len(garbage)):
            z = garbage[i]
            
            m = i if 'M' in z else m
            p = i if 'P' in z else p
            g = i if 'G' in z else g
            
            x += len(z)
            
        return x + sum(travel[0:m]) + sum(travel[0:p]) + sum(travel[0:g])
    
solution = Solution()
actual = solution.garbageCollection(["MMM","PGM","GP"], [3,10])
print(actual)
print(actual == 37)
