from typing import List

class Solution:
    def maximumWealth(self, accounts: List[List[int]]) -> int:
        richest = 0
        
        for acc in accounts:
            wealth = 0
            
            for money in acc:
                wealth += money
                
            if wealth > richest:
                richest = wealth
        
        return richest
    
solution = Solution()
actual = solution.maximumWealth([[1,5],[7,3],[3,5]])
print(actual)
print(actual == 10)
