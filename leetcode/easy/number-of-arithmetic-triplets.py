from typing import List

class Solution:
    def arithmeticTriplets(self, nums: List[int], diff: int) -> int:
        count = 0
        
        for i in range(len(nums)):
            x = 1
            y = nums[i]
            
            for j in range(i+1, len(nums)):
                if nums[j] - y == diff:
                    x += 1
                    y = nums[j]
                    
                if x >= 3:
                    count += 1
                    break
                    
        return count
    
solution = Solution()
actual = solution.arithmeticTriplets([0,1,4,6,7,10], 3)
print(actual)
print(actual == 2)
