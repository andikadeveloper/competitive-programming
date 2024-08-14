from typing import List
import math

class Solution:
    def sumOfSquares(self, nums: List[int]) -> int:
        x = 0
                
        for i in range(1, int(math.sqrt(len(nums))) + 1):
            if len(nums) % i == 0:
                x += nums[i-1] ** 2
                if i != len(nums) // i:
                    x += nums[(len(nums) // i) - 1] ** 2
                
        return x
    
solution = Solution()
actual = solution.sumOfSquares([1, 2, 3, 4])
print(actual)
print(actual == 21)
