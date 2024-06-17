from typing import List

class Solution:
    def createTargetArray(self, nums: List[int], index: List[int]) -> List[int]:
        result = []
        
        for i in range(len(nums)):
            result.insert(index[i], nums[i])
            
        return result
    
    
solution = Solution()
actual = solution.createTargetArray([0,1,2,3,4], [0,1,2,2,1])
print(actual)
print(actual == [0,4,1,3,2])
