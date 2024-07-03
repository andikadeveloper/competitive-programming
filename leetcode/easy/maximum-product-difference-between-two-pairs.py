from typing import List

class Solution:
    def maxProductDifference(self, nums: List[int]) -> int:
        nums.sort()
        
        return (nums[len(nums) - 1] * nums[len(nums) - 2]) - (nums[0] * nums[1])

solution = Solution()
actual = solution.maxProductDifference([5,6,2,7,4])
print(actual)
print(actual == 34)
