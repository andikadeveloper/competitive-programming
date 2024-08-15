from typing import List

class Solution:
    def addedInteger(self, nums1: List[int], nums2: List[int]) -> int:
        nums1.sort()
        nums2.sort()
        
        return nums2[0] - nums1[0]
    
solution = Solution()
actual = solution.addedInteger([2,6,4], [9,7,5])
print(actual)
print(actual == 3)
