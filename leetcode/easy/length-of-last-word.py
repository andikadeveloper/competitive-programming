class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        words = s.split(' ')
        count = len(words) - 1
        
        while count > -1:
            word = words[count]
            
            if word != '':
                return len(word)
            
            count -= 1
        
solution = Solution()

print(solution.lengthOfLastWord("a"))