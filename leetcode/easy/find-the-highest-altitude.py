from typing import List

class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        x = 0
        y = 0
        
        for g in gain:
            y += g
            
            if y > x:
                x = y
                
        return x
    
solution = Solution()
actual = solution.largestAltitude([-5,1,5,0,-7])
print(actual)
print(actual == 1)
