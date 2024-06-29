from typing import List

class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        p = [i for i in range(1, m+1)]
        result = []
        
        for i in queries:
            index = p.index(i)
            result.append(index)
            
            p.insert(0, p.pop(index))
        
        return result
    
solution = Solution()
actual = solution.processQueries([3,1,2,1], 5)
print(actual)
print(actual == [2,1,2,1] )
