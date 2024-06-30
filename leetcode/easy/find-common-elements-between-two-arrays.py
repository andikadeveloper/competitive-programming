from typing import List

class Solution:
    def countExistNum(self, arr, target):
        x = 0
        i = 0
        j = len(arr) - 1
        
        while i <= j:
            if arr[i] in target:
                x += 1
                
            i += 1
            
            if i > j:
                break
                
            if arr[j] in target:
                x += 1
            
            j -= 1
                
        return x
    
    def findIntersectionValues(self, nums1: List[int], nums2: List[int]) -> List[int]:
        return [self.countExistNum(nums1, nums2), self.countExistNum(nums2, nums1)]
    
solution = Solution()
actual = solution.findIntersectionValues([2,3,2], [1,2])
print(actual)
print(actual == [2, 1])
