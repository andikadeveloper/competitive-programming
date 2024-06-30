from typing import List

class Solution:
    def sumOddLengthSubarrays(self, arr: List[int]) -> int:
        z = 0
        
        for i in range(len(arr)):
            x = 1
            y = 0
            
            for j in range(i, len(arr)):
                y += arr[j]
                
                if x % 2 != 0:
                    z += y
                    
                x += 1
                    
        return z
    
solution = Solution()
actual = solution.sumOddLengthSubarrays([1,4,2,5,3])
print(actual)
print(actual == 58)
