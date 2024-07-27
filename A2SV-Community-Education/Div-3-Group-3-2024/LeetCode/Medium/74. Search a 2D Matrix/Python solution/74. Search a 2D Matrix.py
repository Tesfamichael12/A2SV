class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        L, R = 0, ROWS * COLS - 1
        
        while L <= R:
            mid = L + (R - L) // 2 # this way we can avoide any overflows
            row = mid // COLS 
            col = mid % COLS
            if matrix[row][col] == target:
                return True 
            elif matrix[row][col] > target:
                R = mid - 1
            else:
                L = mid + 1
        
        return False # If not found

# NOTE
'''
The intuition is: First visualise the matrix as if it was a list of 1D numbers and
 then run BS on it, after that determine the location of that number in the
 2D matrix using mid // COLS to get the row of the number in the 2D and
 mid % COLS to get the column number of that number. The rest is the same as that of BS.
'''