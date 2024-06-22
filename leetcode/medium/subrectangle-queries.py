from typing import List

class SubrectangleQueries:
    
    def __init__(self, rectangle: List[List[int]]):
        self.rectangle = rectangle

    def updateSubrectangle(self, row1: int, col1: int, row2: int, col2: int, newValue: int) -> None:
        row_last = row2
        
        for i in range(row1, row2 + 1):
            col_last = col2
            
            for j in range(col1, col2 + 1):
                if i > row_last and j > col_last:
                    return
                
                self.rectangle[i][j] = newValue
                self.rectangle[row_last][col_last] = newValue
                
                col_last -= 1
                
            row_last -= 1
                
    def getValue(self, row: int, col: int) -> int:
        return self.rectangle[row][col]
