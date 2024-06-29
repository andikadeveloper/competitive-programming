from typing import List

class Solution:
    def differenceOfSum(self, nums: List[int]) -> int:
        sums = 0
        digits = 0
        
        for num in nums:
            sums += num
            
            for digit in str(num):
                digits += int(digit)
                
        return sums - digits

solution = Solution()
actual = solution.differenceOfSum([1,15,6,3])
print(actual)
print(actual == 9)
