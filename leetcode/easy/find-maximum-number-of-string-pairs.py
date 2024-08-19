from typing import List
from collections import deque

class Solution:
    def isWordSame(self, a: str, b: str):
        if len(a) != len(b) or a[0] != b[len(b)-1]:
            return False
        
        j = len(a) - 1
        for i in range(len(a)):
            if a[i] != b[j]:
                return False
            
            if i >= j:
                return True
            
            j -= 1
        
        return True
    
    def maximumNumberOfStringPairs(self, words: List[str]) -> int:
        l = len(words)
        if l < 2:
            return 0
        
        if l == 2 and words[0][0] != words[1][l-1]:
            return 0
        
        d = deque(words)
        del words
        del l
        x = 0
        
        while len(d) > 1:
            a = d.popleft()
            
            for _ in range(len(d)):
                if self.isWordSame(a, d[0]):
                    d.popleft()
                    x += 1
                    break
                else:
                    d.append(d.popleft())
                
        return x
                    
solution = Solution()
actual = solution.maximumNumberOfStringPairs(["cd","ac","dc","ca","zz"])
print(actual)
print(actual == 2)
