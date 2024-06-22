from typing import List

class Solution:
    def minMovesToSeat(self, seats: List[int], students: List[int]) -> int:
        seats = sorted(seats)
        students = sorted(students)
        
        result = 0
        j = len(seats) - 1
        
        for i in range(len(seats)):
            if len(seats) % 2 == 0 and i >= j:
                break
                
            result += abs(seats[i] - students[i])
            
            if len(seats) % 2 != 0 and i >= j:
                break
                    
            result += abs(seats[j] - students[j])
            
            j -= 1
            
        return result
    
solution = Solution()
actual = solution.minMovesToSeat([3,1,5], [2,7,4])
print(actual)
print(actual == 4)
