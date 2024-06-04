from typing import List

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        x = "".join(str(x) for x in digits)
        
        y = int(x) + 1
        
        return [int(x) for x in str(y)]
        
solution = Solution()

print(solution.plusOne([1,2,3]))