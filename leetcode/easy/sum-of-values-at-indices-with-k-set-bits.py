from typing import List

class Solution:
    def sumIndicesWithKSetBits(self, nums: List[int], k: int) -> int:
        result = 0
        
        for i in range(len(nums)):
            if bin(i)[2:].count('1') == k:
                result += nums[i]
        
        return result
    
solution = Solution()
actual = solution.sumIndicesWithKSetBits([5,10,1,5,2], 1)
print(actual)
print(actual == 13)
