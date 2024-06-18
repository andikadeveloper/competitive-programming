from typing import List

class Solution:
    def numberGame(self, nums: List[int]) -> List[int]:
        nums = sorted(nums)
        arr = []
        
        for i in range(0, len(nums), 2):
            arr.append(nums[i + 1])
            arr.append(nums[i])
            
        return arr
    
solution = Solution()
actual = solution.numberGame([5,4,2,3])
print(actual)
print(actual == [3,2,5,4])
