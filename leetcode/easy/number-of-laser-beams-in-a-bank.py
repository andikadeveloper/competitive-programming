from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev_beam = 0
        laser = 0
        
        for beams in bank:
            total_beam = 0
            for beam in beams:
                total_beam += int(beam)
                
            if total_beam != 0:
                laser += (total_beam * prev_beam)
                prev_beam = total_beam
            
        return laser
    
solution = Solution()
actual = solution.numberOfBeams(["011001","000000","010100","001000"])
print(actual)
print(actual == 8)
