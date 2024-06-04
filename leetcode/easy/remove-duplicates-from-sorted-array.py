from typing import List

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        prev = None
        count = 0
        
        while count < len(nums):
            num = nums[count]
            
            if num == prev:
                nums.pop(count)
            else:
                prev = num
                count += 1
                
        return len(nums)
    
solution = Solution()

print(solution.removeDuplicates([0,0,1,1,1,2,2,3,3,4]))