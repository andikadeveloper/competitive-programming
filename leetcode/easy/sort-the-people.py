from typing import List

class Solution:
    def sortPeople(self, n: List[str], h: List[int]) -> List[str]:
        x = dict(zip(h, n))
        
        h.sort(reverse=True)
        
        return [x[i] for i in h]
    
solution = Solution()
actual = solution.sortPeople(["Mary","John","Emma"], [180,165,170])
print(actual)
print(actual == ["Mary","Emma","John"])
