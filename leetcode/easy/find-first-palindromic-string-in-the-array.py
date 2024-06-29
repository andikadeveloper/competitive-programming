from typing import List

class Solution:
    def isPalindrome(self, word: str) -> bool:
        i = 0
        j = len(word) - 1
        
        while i < j:
            if word[i] != word[j]:
                return False

            i += 1
            j -= 1

        return True
    
    def firstPalindrome(self, words: List[str]) -> str:
        for word in words:
            if self.isPalindrome(word):
                return word
                
        return ''
    
solution = Solution()
actual = solution.firstPalindrome(["abc","car","ada","racecar","cool"])
print(actual)
print(actual == "ada")
