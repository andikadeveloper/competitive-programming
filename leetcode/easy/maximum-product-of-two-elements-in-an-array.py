from typing import List


class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        nums.sort()

        return (nums[len(nums) - 1] - 1) * (nums[len(nums) - 2] - 1)


solution = Solution()
actual = solution.maxProduct([3, 4, 5, 2])
print(actual)
print(actual == 12)
