from typing import List

class Solution:
    def onesMinusZeros(self, grid: List[List[int]]) -> List[List[int]]:
        result = []
        
        data = {
            'col': {},
            'row': {},
        }
        
        for i in range(len(grid)):
            row = grid[i]
            
            diff_arr = []
            
            for j in range(len(row)):
                one_row = 0
                one_col = 0
                
                if i in data['row']:
                    one_row = data['row'][i]
                else:
                    for x in range(len(row)):
                        if row[x] == 1:
                            one_row += 1
                    
                    data['row'][i] = one_row
                
                if j in data['col']:
                    one_col = data['col'][j]
                else:
                    for y in range(len(grid)):
                        if grid[y][j] == 1:
                            one_col += 1
                            
                    data['col'][j] = one_col
                
                diff = one_row + one_col - (len(row) - one_row) - (len(grid) - one_col)
                
                diff_arr.append(diff)
                
            result.append(diff_arr)
                
        return result

solution = Solution()
actual = solution.onesMinusZeros([[0,1,1],[1,0,1],[0,0,1]])
print(actual)
print(actual == [[0,0,4],[0,0,4],[-2,-2,2]])
