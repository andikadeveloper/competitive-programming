from typing import List


class Solution:
    def sumCounts(self, nums: List[int]) -> int:
        x = 0

        for i in range(len(nums)):
            for j in range(i, len(nums) + 1):
                x += len(set(nums[i:j])) ** 2

        return x


solution = Solution()
actual = solution.sumCounts([1, 2, 1])
print(actual)
print(actual == 15)
