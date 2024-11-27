from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        row = len(matrix)
        col = len(matrix[0])
        spiral = []
        row_up, row_down = 0, row-1
        col_left, col_right = 0, col-1
        while row_up <= row_down and col_left <= col_right:
            # traverse right
            for i in range(col_left, col_right+1):
                spiral.append(matrix[row_up][i])
            row_up += 1
            
            #traverse down
            for i in range(row_up, row_down+1):
                spiral.append(matrix[i][col_right])
            col_right -= 1

            # tarverse left
            if row_up <= row_down:
                for i in range(col_right, col_left-1,-1):
                    spiral.append(matrix[row_down][i])
                row_down -= 1

            #traverse up
            if col_left <= col_right:
                for i in range(row_down, row_up-1,-1):
                    spiral.append(matrix[i][col_left])
                col_left += 1
        return spiral


        