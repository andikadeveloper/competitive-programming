from typing import List

class Solution:
    def rearrangeArray(self, nums: List[int]) -> List[int]:
        p = []
        n = []
        
        for num in nums:
            if num > 0:
                p.append(num)
            else:
                n.append(num)
                
        for i in range(len(p)):
            nums[i * 2] = p[i]
            nums[(i * 2) + 1] = n[i]
                
        return nums
    
solution = Solution()
actual = solution.rearrangeArray([3,1,-2,-5,2,-4])
print(actual)
print(actual == [3,-2,1,-5,2,-4])
