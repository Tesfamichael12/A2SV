class Solution {
public:
    vector<vector<int>> largestLocal(vector<vector<int>>& grid) {
        int n = grid.size();
        vector<vector<int>> maxLocal(n - 2, vector<int>(n - 2));

        for (int i = 0; i < n - 2; i++)
        {
            for (int j = 0; j < n - 2; j++)
            {
                int maxval = 0; // since the constraint told us that the valuse are greater then 1
                for (int row = i; row < i + 3; row++)
                {
                    for (int col = j; col < j + 3; col++)
                    {
                         maxval = max(maxval, grid[row][col]);
                    }
                }
                maxLocal[i][j] = maxval;
            }
        }
        return maxLocal;
    }
};

// # Or we can calculate the maxval by precalculating the max using the following method 
// # It is important to note that the following method is not scalable but the above method is, we can change 3 to any value say k which can be any value of a contigious K x K matrix

//  # Calculate the maximum value for the 3x3 grid starting at (i, j) This mehtod is not scalable
//                 # maxval = max(
//                 #     grid[i][j], grid[i][j+1], grid[i][j+2],
//                 #     grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],
//                 #     grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]
//                 # )