from typing import List

class Solution:
    def findSmallestIndex(self, nums: List[int]):
        s = nums[0]
        si = 0
        for i in range(1, len(nums)):
            if nums[i] < s:
                s = nums[i]
                si = i
                
        return si
    
    def getFinalState(self, nums: List[int], k: int, multiplier: int) -> List[int]:
        for i in range(k):
            index = self.findSmallestIndex(nums)
            
            nums[index] = nums[index] * multiplier
            
        return nums

solution = Solution()
actual = solution.getFinalState([2,1,4,1,4], 4, 3)
print(actual)
print(actual == [6,9,4,3,4])
