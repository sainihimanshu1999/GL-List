'''In this question we have to find the longest increasing path in the matrix, the basic point we have to keep in 
mind that, at every instant we have recurse because of all the possibilities of direction it would have to move in'''

def longestIncreasingPath(grid):
    m = len(grid)
    n = len(grid[0])

    dp = [[0]*n for _ in range(m)]

    def dfs(i,j):
        if not dp[i][j]:
            val = grid[i][j]

            if i and val>grid[i-1][j]:
                up = dfs(i-1,j)
            else:
                up= 0

            if i<m-1 and val>grid[i+1][j]:
                down = dfs(i+1,j)
            else:
                down = 0

            if j and val>grid[i][j-1]:
                left = dfs(i,j-1)
            else:
                left = 0

            if j<n-1 and val>grid[i][j+1]:
                right = dfs(i,j+1)
            else:
                right = 0

            dp[i][j] = 1+ max(up,down,left,right)
        return dp[i][j]

    result = []
    for i in range(m):
        for j in range(n):
            result.append(dfs(i,j))

    return max(result)


matrix = [[9,9,4],[6,6,8],[2,1,1]]
print(longestIncreasingPath(matrix))