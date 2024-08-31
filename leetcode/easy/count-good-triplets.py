from typing import List

class Solution:
    def countGoodTriplets(self, arr: List[int], a: int, b: int, c: int) -> int:
        x = 0
        
        for i in range(len(arr)):            
            for j in range(i+1, len(arr)):                
                if abs(arr[i] - arr[j]) > a:
                    continue
                    
                for k in range(j+1, len(arr)):
                    if abs(arr[j] - arr[k]) > b or abs(arr[i] - arr[k]) > c:
                        continue
                    
                    x += 1
        return x

solution = Solution()
actual = solution.countGoodTriplets([3,0,1,1,9,7], 7, 2, 3)
print(actual)
print(actual == 4)
