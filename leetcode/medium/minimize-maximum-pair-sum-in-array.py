from typing import List

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        
        l = len(nums) - 1
        x = 0
        for i in range(len(nums)):
            if i > l:
                break
            
            y = nums[l] + nums[i]
            if y > x:
                x = y
                
            del y
            
            l -= 1
        
        return x
    
solution = Solution()
actual = solution.minPairSum([3,5,2,3])
print(actual)
print(actual == 7)
