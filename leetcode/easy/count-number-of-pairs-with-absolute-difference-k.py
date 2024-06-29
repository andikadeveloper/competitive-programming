from typing import List

class Solution:
    def countKDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        z = 0
        x = {}
        
        for i in range(len(nums)):
            num = nums[i]
            
            if num in x:
                z += x[num]
            
            y = num + k
            if y in x:
                x[y] += 1
            else:
                x[y] = 1
                    
        return z
    
solution = Solution()
actual = solution.countKDifference([3,2,1,5,4], 2)
print(actual)
print(actual == 3)
