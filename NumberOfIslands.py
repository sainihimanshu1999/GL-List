'''We use dfs in this question, maintain a count and count all the cluster of ones'''


def islands(matrix):
    m= len(matrix)
    n = len(matrix[0])

    count = 0

    for i in range(m):
        for j in range(n):
            if matrix[i][j] == '1':
                dfs(i,j,m,n,matrix)
                count+=1
    
    return count


def dfs(i,j,m,n,grid):
    if 0<=i<m and 0<=j<n and grid[i][j]=='1':
        grid[i][j]='0'
        dfs(i+1,j,m,n,grid)
        dfs(i-1,j,m,n,grid)
        dfs(i,j+1,m,n,grid)
        dfs(i,j-1,m,n,grid)

    return False


grid = [
  ["1","1","0","0","0"],
  ["1","1","0","0","0"],
  ["0","0","1","0","0"],
  ["0","0","0","1","1"]
]

print(islands(grid))