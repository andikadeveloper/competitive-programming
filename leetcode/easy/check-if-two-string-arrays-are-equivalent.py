from typing import List

class Solution:
    def arrayStringsAreEqual(self, word1: List[str], word2: List[str]) -> bool:
        x = ''
        y = ''
        
        z = len(word1) if len(word1) > len(word2) else len(word2)
        
        for i in range(z):
            if i < len(word1):
                x += word1[i]   
            
            if i < len(word2):
                y += word2[i]
            
        return x == y
    
solution = Solution()
actual = solution.arrayStringsAreEqual(["abc", "d", "defg"], ["abcddefg"])
print(actual)
print(actual == True)
