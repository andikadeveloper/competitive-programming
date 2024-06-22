from typing import List

class Solution:
    def countMatches(self, items: List[List[str]], ruleKey: str, ruleValue: str) -> int:
        spec = {
            'type': 0,
            'color': 1,
            'name': 2
        }
        
        count = 0
        
        j = len(items) - 1
        
        for i in range(len(items)):
            if len(items) % 2 == 0 and i >= j:
                break
            
            if items[i][spec[ruleKey]] == ruleValue:
                count += 1
                
            if len(items) % 2 != 0 and i >= j:
                break
                
            if items[j][spec[ruleKey]] == ruleValue:
                count += 1
                
            j -= 1
        
        return count
    
solution = Solution()
actual = solution.countMatches([["phone","blue","pixel"],["computer","silver","lenovo"],["phone","gold","iphone"]], 'color', 'silver')
print(actual)
print(actual == 1)
