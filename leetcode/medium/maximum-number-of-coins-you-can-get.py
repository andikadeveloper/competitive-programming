from typing import List

class Solution:
    def maxCoins(self, piles: List[int]) -> int:
        piles.sort()
        
        result = 0
        
        for i in range(len(piles) // 3, len(piles), 2):
            result += piles[i]
            
        return result
    
solution = Solution()
actual = solution.maxCoins([2,4,1,2,7,8])
print(actual)
print(actual == 9)
