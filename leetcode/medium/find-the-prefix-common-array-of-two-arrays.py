from typing import List

class Solution:
    def findThePrefixCommonArray(self, A: List[int], B: List[int]) -> List[int]:
        x = []
        last = 0
        temp_a = []
        temp_b = []
        
        for i in range(len(A)):
            temp_a.append(A[i])
            temp_b.append(B[i])
            
            y = 0
            j = 0
            
            while j < len(temp_a):
                a = temp_a[j]
                
                if a in temp_b:
                    y += 1
                    temp_a.remove(a)
                    temp_b.remove(a)
                else:
                    j += 1
            
            last += y
            x.append(last)
            
        return x

solution = Solution()
actual = solution.findThePrefixCommonArray([1,3,2,4], [3,1,2,4])
print(actual)
print(actual == [0,2,3,4])
