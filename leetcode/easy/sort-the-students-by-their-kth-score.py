from typing import List

class Solution:
    def quickSort(self, s, k):
        if len(s) < 2:
            return s
        
        p = s[0]
        
        l = []
        g = []
        
        for q in s[1:]:
            if q[k] <= p[k]:
                l.append(q)
            else:
                g.append(q)
                
        return self.quickSort(g, k) + [p] + self.quickSort(l, k)
    
    def sortTheStudents(self, score: List[List[int]], k: int) -> List[List[int]]:
        return self.quickSort(score, k)
    
solution = Solution()
actual = solution.sortTheStudents([[10,6,9,1],[7,5,11,2],[4,8,3,15]], 2)
print(actual)
print(actual == [[7,5,11,2],[10,6,9,1],[4,8,3,15]])
