from typing import List

class Solution:
    def diagonalSort(self, mat: List[List[int]]) -> List[List[int]]:
        diagonal = {}
        
        for i in range(len(mat)):
            nums = mat[i]
            
            for j in range(len(nums)):
                if i == 0 or j == 0:
                    diagonal[i-j] = [nums[j]]
                    continue
                
                diagonal[i-j].append(nums[j])
                
        for values in diagonal.values():
            values.sort()
            
        current_index = {key: 0 for key in diagonal.keys()}
            
        for i in range(len(mat)):
            nums = mat[i]
            
            for j in range(len(nums)):
                mat[i][j] = diagonal[i-j][current_index[i-j]]
                current_index[i-j] += 1
        
        return mat

solution = Solution()
actual = solution.diagonalSort([[3,3,1,1],[2,2,1,2],[1,1,1,2]])
print(actual)
print(actual == [[1,1,1,1],[1,2,2,2],[1,2,3,3]])