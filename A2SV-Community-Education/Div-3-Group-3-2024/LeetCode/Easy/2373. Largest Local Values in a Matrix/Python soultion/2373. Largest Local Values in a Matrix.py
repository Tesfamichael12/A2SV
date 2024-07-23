class Solution:
    def largestLocal(self, grid: List[List[int]]) -> List[List[int]]:
        n = len(grid)
        maxLocal = [[0] * (n - 2) for _ in range(n - 2)]

        for i in range(n - 2): # since the grid is a square matrix
            for j in range(n - 2):
                maxval = 0
                for row in range(i, i+3):
                    for col in range(j, j+3):
                        maxval = max(maxval, grid[row][col])
            
                maxLocal[i][j] = maxval
        
        return maxLocal

# Or we can calculate the maxval by precalculating the max using the following method 
# It is important to note that the following method is not scalable but the above method is, we can change 3 to any value say k which can be any value of a contigious K x K matrix

 # Calculate the maximum value for the 3x3 grid starting at (i, j) This mehtod is not scalable
                # maxval = max(
                #     grid[i][j], grid[i][j+1], grid[i][j+2],
                #     grid[i+1][j], grid[i+1][j+1], grid[i+1][j+2],
                #     grid[i+2][j], grid[i+2][j+1], grid[i+2][j+2]
                # )