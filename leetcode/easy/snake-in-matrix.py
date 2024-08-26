from typing import List

class Solution:
    def finalPositionOfSnake(self, n: int, commands: List[str]) -> int:
        p = 0
        for c in commands:            
            match c:
                case "LEFT":
                    p += -1
                case "UP":
                    p += -n
                case "RIGHT":
                    p += 1
                case "DOWN":
                    p += n
            
        return p
    

solution = Solution()
actual = solution.finalPositionOfSnake(3, ["DOWN","RIGHT","UP"])
print(actual)
print(actual == 1)
