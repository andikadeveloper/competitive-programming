from typing import List

class Solution:
    def maximizeSum(self, nums: List[int], k: int) -> int:
        nums.sort()
        total = 0
        
        for i in range(k):
            last = nums.pop(len(nums)-1)
            total += last
            nums.append(last+1)
        return total
    
solution = Solution()
actual = solution.maximizeSum([1,2,3,4,5], 3)
print(actual)
print(actual == 18)
