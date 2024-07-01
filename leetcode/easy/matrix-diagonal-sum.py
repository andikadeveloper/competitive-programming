from typing import List

class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        x = 0
        i = 0
        j = len(mat[0]) - 1
        l = len(mat) - 1
        
        for f in range(len(mat)):
            if f > l:
                return x
            
            if i >= (len(mat[f]) // 2) and len(mat[f]) % 2 != 0:
                x += mat[f][i]
            else:
                x += mat[f][i] + mat[f][j] + mat[l][i] + mat[l][j]
            
            i += 1
            j -= 1
            l -= 1
            
        return x

solution = Solution()
actual = solution.diagonalSum([[1,2,3], [4,5,6], [7,8,9]])
print(actual)
print(actual == 25)
