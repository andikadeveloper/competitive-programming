from typing import List

class Solution:
    def uniqueMorseRepresentations(self, words: List[str]) -> int:
        morses = {
            'a': '.-', 'b': '-...', 'c': '-.-.', 'd': '-..', 'e': '.', 'f': '..-.', 'g': '--.', 'h': '....', 
            'i': '..', 'j': '.---', 'k': '-.-', 'l': '.-..', 'm': '--', 'n': '-.', 'o': '---', 'p': '.--.', 
            'q': '--.-', 'r': '.-.', 's': '...', 't': '-', 'u': '..-', 'v': '...-', 'w': '.--', 'x': '-..-', 
            'y': '-.--', 'z': '--..'
        }
        
        result = {}
        
        for word in words:
            morse = ''
            
            for letter in word:
                morse += morses[letter]
                
            result[morse] = 1
            
        return len(result)
    
solution = Solution()
actual = solution.uniqueMorseRepresentations(["gin", "zen", "gig", "msg"])
print(actual)
print(actual == 2)
