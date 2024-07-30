def solve():
    n, m = map(int, input().split())
    grid = [list(map(int, input().split())) for _ in range(n)]

    maxval = 0

    for i in range(n):
        for j in range(m):
            temp = grid[i][j]
            
            # go up and left 
            tempi = i - 1
            tempj = j - 1
            while tempi >= 0 and tempj >= 0:
                temp += grid[tempi][tempj]
                tempi -= 1
                tempj -= 1
            
            # go down and right
            tempi = i + 1
            tempj = j + 1
            while tempi < n and tempj < m:
                temp += grid[tempi][tempj]
                tempi += 1
                tempj += 1
            
            # go up and right
            tempi = i - 1
            tempj = j + 1
            while tempi >= 0 and tempj < m:
                temp += grid[tempi][tempj]
                tempi -= 1
                tempj += 1

            # go down and left 
            tempi = i + 1
            tempj = j - 1
            while tempi < n and tempj >= 0:
                temp += grid[tempi][tempj]
                tempi += 1
                tempj -= 1

            maxval = max(maxval, temp)
    
    print(maxval)


if __name__ == "__main__":
    t = int(input())
    for _ in range(t):
        solve()