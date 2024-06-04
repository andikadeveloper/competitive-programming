class Solution:
    def mySqrt(self, x: int) -> int:
        odd = 1
        count = 0
        
        while True:
            x -= odd
            odd += 2
            count += 1
            
            if x < 0:
                return count - 1
        
        return count
        
solution = Solution()

print(solution.mySqrt(8))