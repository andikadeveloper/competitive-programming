from typing import List

class Solution:
    def pivotArray(self, nums: List[int], pivot: int) -> List[int]:
        l = []
        p = []
        g = []
        
        for num in nums:
            if num < pivot:
                l.append(num)
            elif num == pivot:
                p.append(num)
            else:
                g.append(num)
                
        return l + p + g
    
solution = Solution()
actual = solution.pivotArray([9, 12, 3, 5, 14, 10, 10], 10)
print(actual)
print(actual == [9, 3, 5, 10, 10, 12, 14])
