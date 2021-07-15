'''In this question we will do simple bfs by simply maintaining a viisited set for pacific and atlantic ocean
in this solution we will reverse and move increasing way and check till which points ocean can reach'''


def pacificAtlantic(matrix):
    m = len(matrix)
    n = len(matrix[0])

    pacific = set()
    atlantic = set()

    directions = [(1,0),(0,1),(-1,0),(0,-1)]

    def dfs(i,j,visited):
        if (i,j) in visited:
            return 
        
        visited.add((i,j))

        for d in directions:
            x,y = i+d[0],j+d[1]

            if 0<=x<m and 0<=y<n and matrix[x][y]>=matrix[i][j]:
                dfs(x,y,visited)


    for i in range(m):
        dfs(i,0,pacific)
        dfs(i,n-1,atlantic)

    for j in range(n):
        dfs(0,j,pacific)
        dfs(m-1,j,atlantic)

    return list(pacific&atlantic)

heights = [[1,2,2,3,5],[3,2,3,4,4],[2,4,5,3,1],[6,7,1,4,5],[5,1,1,2,4]]
print(pacificAtlantic(heights))


