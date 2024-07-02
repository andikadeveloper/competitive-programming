from typing import List

class Solution:
    def isAcronym(self, words: List[str], s: str) -> bool:
        if len(words) != len(s):
            return False
        
        for i in range(len(words)):
            if words[i][0] != s[i]:
                return False
            
        return True

solution = Solution()
actual = solution.isAcronym(["alice","bob","charlie"], "abc")
print(actual)
print(actual == True)
