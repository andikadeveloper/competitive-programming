from typing import List

class Solution:
    def finalValueAfterOperations(self, operations: List[str]) -> int:
        result = 0
        
        for o in operations:
            if o == '++X' or o == 'X++':
                result += 1
            else:
                result -= 1
                
        return result
    
solution = Solution()
print(solution.finalValueAfterOperations(["--X","X++","X++"]))
