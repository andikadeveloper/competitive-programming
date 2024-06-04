from typing import List

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        count = 0
        
        while count < len(nums):
            num = nums[count]
            
            if num == val:
                nums.pop(count)
            else:
                count += 1
                
        return len(nums)
    
solution = Solution()

print(solution.removeElement([0,1,2,2,3,0,4,2], 2))