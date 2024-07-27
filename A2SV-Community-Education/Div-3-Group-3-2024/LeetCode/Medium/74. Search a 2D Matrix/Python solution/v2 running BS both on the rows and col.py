class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        ROWS, COLS = len(matrix), len(matrix[0])
        top, bot = 0, ROWS - 1
        while top <= bot:
            mid_row = (top + bot) // 2
            if matrix[mid_row][0] > target:
                bot = mid_row - 1 
            elif matrix[mid_row][-1] < target:
                top = mid_row + 1
            else:
                break
        if top > bot:
            return False
        mid_row = (top + bot) // 2 # update mid_row since now top == bot i.e mid_row = top = bot
        L, R = 0, COLS - 1
        while L <= R:
            mid = (L + R) // 2
            if matrix[mid_row][mid] == target:
                return True
            elif matrix[mid_row][mid] > target:
                R = mid - 1
            else:
                L = mid + 1
        return False # If not found



# NOTE
'''
The intuition : Since the matrix is alrady sorted we can run BS on the rows to get the row 
at which the target is located or bounded, then run BS in that row. Therefore the Time Complexity of this algorithm will be log ROWS plus log COLS : O(log m + log n) = O(log(m * n)) where m is rows and n is cols of the matrix.
'''