class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int ROWS = matrix.size(), COLS = matrix[0].size();
        int top = 0, bot = ROWS - 1;
        while (top <= bot)
        {
            int mid_row = (top + bot) / 2;
            
            if (matrix[mid_row][0] > target)
                bot = mid_row - 1;
            else if (matrix[mid_row][COLS - 1] < target)
                top = mid_row + 1;
            else
                break;
        }
        if (top > bot)
           return false;
        int mid_row = (top + bot) / 2; // update mid_row since now top == bot i.e mid_row = top = bot
        int L = 0, R = COLS - 1;
        while (L <= R)
        {
            int mid = (L + R) / 2;
            if (matrix[mid_row][mid] == target) 
                return true;
            else if (matrix[mid_row][mid] > target)
                R = mid - 1;
            else
                L = mid + 1;
        }
        return false; // If not found
    }
};

/*
NOTE
'''
The intuition : Since the matrix is alrady sorted we can run BS on the rows to get the row 
at which the target is located or bounded, then run BS in that row. Therefore the Time Complexity of this algorithm will be log ROWS plus log COLS : O(log m + log n) = O(log(m * n)) where m is rows and n is cols of the matrix.
'''
*/