from typing import List

class Solution:
    def findWordsContaining(self, words: List[str], x: str) -> List[int]:
        result = []
        
        for i in range(len(words)):
            word = words[i]
            
            for letter in word:
                if letter == x:
                    result.append(i)
                    break
        
        return result
    
solution = Solution()
actual = solution.findWordsContaining(["abc","bcd","aaaa","cbc"], "a")
print(actual)
print(actual == [0,2])