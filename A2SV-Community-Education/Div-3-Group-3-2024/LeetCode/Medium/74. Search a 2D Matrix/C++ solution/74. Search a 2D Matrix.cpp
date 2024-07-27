class Solution {
public:
    bool searchMatrix(vector<vector<int>>& matrix, int target) {
        int ROWS = matrix.size(), COLS = matrix[0].size();
        int L = 0, R = ROWS * COLS - 1;
        while (L <= R)
        {
            int mid = L + (R - L) / 2; // To avoid any over flows
            int row = mid / COLS, col = mid % COLS;
            
            if (matrix[row][col] == target)
                return true;
            else if (matrix[row][col] > target)
                R = mid - 1;
            else
                L = mid + 1;
        }
        return false; // If not found
    }
};