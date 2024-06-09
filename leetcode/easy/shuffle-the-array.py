from typing import List

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        first_pointer = nums[0:n]
        second_pointer = nums[n:len(nums)]
        
        result = []
        
        for i in range(len(first_pointer)):
            result.extend([first_pointer[i], second_pointer[i]])
        
        return result
        
solution = Solution()
actual = solution.shuffle([1,2,3,4,4,3,2,1], 4)

print(actual)
print(actual == [1,4,2,3,3,2,4,1])
