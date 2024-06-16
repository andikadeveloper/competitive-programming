from typing import List

class Solution:
    def leftRightDifference(self, nums: List[int]) -> List[int]:
        result = []
        left = 0
        right = sum(nums)
        
        for i in range(len(nums)):
            right -= nums[i]
            result.append(abs(left - right))
            left += nums[i]
        
        return result
        
solution = Solution()
actual = solution.leftRightDifference([10,4,8,3])
print(actual)
print(actual == [15,1,11,22])