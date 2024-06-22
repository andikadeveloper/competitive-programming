from typing import List

class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        result = []
        row_index = 0
        
        while (row_index + 3) <= len(grid):
            col_index = 0
            
            while (col_index + 3) <= len(grid[0]):
                max_number = 0
                
                for j in range(row_index, row_index + 3):
                    row = grid[j]
                    max_col = max(row[col_index:col_index + 3])
                    
                    if max_col > max_number:
                        max_number = max_col
                        
                if len(result) <= row_index:
                    result.append([])
                    
                result[row_index].append(max_number)
                col_index += 1
                
            row_index += 1
            
        return result
    
solution = Solution()
actual = solution.largestLocal([[9,9,8,1],[5,6,2,6],[8,2,6,4],[6,2,2,2]])
print(actual)
print(actual == [[9,9],[8,6]])
