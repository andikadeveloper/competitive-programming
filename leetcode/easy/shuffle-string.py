from typing import List

class Solution:
    def restoreString(self, s: str, indices: List[int]) -> str:
        t = [None] * len(s)
        
        for i in range(len(s)):
            t[indices[i]] = s[i]
            
        s = ''
        
        for i in t:
            s += i
            
        return s
    
solution = Solution()
actual = solution.restoreString("codeleet", [4,5,6,7,0,2,1,3])
print(actual)
print(actual == "leetcode")
