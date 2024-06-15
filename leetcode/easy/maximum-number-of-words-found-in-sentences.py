from typing import List

class Solution:
    def mostWordsFound(self, sentences: List[str]) -> int:
        most_sentence = 0
        
        for sentence in sentences:
            count = 1
            
            for letter in sentence:
                if letter == ' ':
                    count += 1
                    
            if count > most_sentence:
                most_sentence = count
                
        return most_sentence
    
solution = Solution()
actual = solution.mostWordsFound(["alice and bob love leetcode", "i think so too", "this is great thanks very much"])
print(actual)
print(actual == 6)
