from typing import List

class Solution:
    def smallerNumbersThanCurrent(self, nums: List[int]) -> List[int]:
        result = []
        
        index = 0
        
        while index < len(nums):
            count = 0
            
            for j in range(1, len(nums)):
                if nums[j] < nums[0]:
                    count += 1
                    
            result.append(count)
            
            nums = nums + [nums[0]]
            nums.pop(0)
            
            index += 1
                
        return result
    
solution = Solution()
actual = solution.smallerNumbersThanCurrent([6,5,4,8])
print(actual)
print(actual == [2,1,0,3])