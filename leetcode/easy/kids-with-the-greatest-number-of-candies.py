from typing import List

class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        greatest = 0
        
        for i in range(len(candies)):
            candy = candies[i]
            
            if candy > greatest:
                greatest = candy
                
            candies[i] = candy + extraCandies
            
        for i in range(len(candies)):
            candy = candies[i]
            
            if candy >= greatest:
                candies[i] = True
            else:
                candies[i] = False
                
        return candies
    
solution = Solution()
actual = solution.kidsWithCandies([2,3,5,1,3], 3)
print(actual)
print(actual == [True,True,True,False,True])
