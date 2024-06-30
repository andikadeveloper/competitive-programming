from typing import List

class Solution:
    def countConsistentStrings(self, allowed: str, words: List[str]) -> int:
        count = 0
        
        for word in words:
            i = 0
            j = len(word) - 1
            
            x = True
            
            while i <= j:
                if word[i] not in allowed or word[j] not in allowed:
                    x = False
                    break
                j -= 1
                
            if x:
                count += 1
                
        return count
    
solution = Solution()
actual = solution.countConsistentStrings("ab", ["ad","bd","aaab","baa","badab"])
print(actual)
print(actual == 2)
