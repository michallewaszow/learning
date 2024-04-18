from typing import List

class NumMatrix:
    #my solution
    def __init__(self, matrix: List[List[int]]):
        self.prefix_sum_rows = []
        self.prefix_sum_rows.append([0 for _ in range(len(matrix[0]) + 1)])
        for r_ix in range(len(matrix)):
            row_sum = 0
            row_prefixes = [0]
            for c_ix, num in enumerate(matrix[r_ix]):
                row_sum += num
                ''' 
                prefix_sum_rows has one additional row on top of matrix, and one additional column on the left, 
                though when we take above sum we are referring to same row index cause its shifted and column index + 1 cause its also shifted 
                '''
                matrix_sum = row_sum + self.prefix_sum_rows[r_ix][c_ix+1]  
                row_prefixes.append(matrix_sum)
            self.prefix_sum_rows.append(row_prefixes)

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        sum_from_region = 0
        # for i in range(row1, row2+1):
        upper_diff = self.prefix_sum_rows[row1-1][col2]
        left_diff = self.prefix_sum_rows[row2][col1-1] - self.prefix_sum_rows[row1-1][col1-1]
        return self.prefix_sum_rows[row2][col2] - upper_diff - left_diff
    
    #more concise 
    def __init__(self, matrix: List[List[int]]):
        ROWS, COLS = len(matrix), len(matrix[0])
        self.sum_matrix = [[0] * (COLS + 1) for _ in range(ROWS + 1)]
        for r in range(ROWS):
            row_prefix_sum = 0
            for c in range(COLS):
                row_prefix_sum += matrix[r][c]
                above = self.sum_matrix[r][c+1]
                self.sum_matrix[r+1][c+1] = row_prefix_sum + above

    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        row1, col1, row2, col2 = row1+1, col1+1, row2+1, col2+1
        bottom_right = self.sum_matrix[row2][col2]
        above = self.sum_matrix[row1 - 1][col2]
        top_left = self.sum_matrix[row1 - 1][col1 - 1]
        left = self.sum_matrix[row2][col1 - 1] - top_left
        return bottom_right - above - left

# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)
obj = NumMatrix([
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9],
    [1, 1, 1]
])    
print(obj.sum_matrix)
print(obj.sumRegion(0, 0, 2, 2))
print(obj.sumRegion(0, 1, 1, 1))