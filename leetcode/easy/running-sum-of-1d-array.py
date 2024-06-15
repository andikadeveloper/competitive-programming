from typing import List

class Solution:
    def runningSum(self, nums: List[int]) -> List[int]:
        result = []
        num_sum = 0
        
        for i in nums:
            num_sum += i
            
            result.append(num_sum)
            
        return result
    
solution = Solution()
actual = solution.runningSum([1,2,3,4])
print(actual)
print(actual == [1,3,6,10])
