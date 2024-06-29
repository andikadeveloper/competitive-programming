from typing import List

class Solution:
    def minimumAverage(self, nums: List[int]) -> float:
        nums.sort()
    
        m = len(nums) // 2
        i = 0
        a = (nums[0] + nums[len(nums) - 1]) / 2
        
        while i <= (m - 1 - i):
            avg = (nums[i] + nums[len(nums) - 1 - i]) / 2
            
            if avg < a:
                a = avg
                
            avg = (nums[m - 1 - i] + nums[m + i]) / 2
            
            if avg < a:
                a = avg
            
            i += 1
            
        return a
    
solution = Solution()
actual = solution.minimumAverage([7,8,3,4,15,13,4,1])
print(actual)
print(actual == 5.5)
