from typing import List

class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        if target > nums[len(nums) - 1]:
            return len(nums)
        
        if target <= nums[0]:
            return 0
        
        for i in range(len(nums)):
            if nums[i] >= target:
                return i
    
solution = Solution()
print(solution.searchInsert([2,3,5,6,9], 7))