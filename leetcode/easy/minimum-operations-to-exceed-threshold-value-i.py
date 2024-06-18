from typing import List

class Solution:
    def minOperations(self, nums: List[int], k: int) -> int:
        nums = sorted(nums)
        
        for i in range(len(nums)):
            if nums[i] >= k:
                return i
            
solution = Solution()
actual = solution.minOperations([2,11,10,1,3], 10)
print(actual)
print(actual == 3)
