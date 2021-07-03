'''The spiral matrix is formed by simple iterations'''

def spiralMatrix(matrix):
    m = len(matrix)
    n = len(matrix[0])

    result = []

    x,y=0,0

    while x<m and y<n:

        for i in range(y,n):
            result.append(matrix[x][i])

        x+=1

        for i in range(x,m):
            result.append(matrix[i][n-1])

        n-=1

        if x<m:
            for i in range(n-1,y-1,-1):
                result.append(matrix[m-1][i])

            m-=1

        if y<n:
            for i in range(m-1,x-1,-1):
                result.append(matrix[i][y])
            y+=1

    return result

matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
print(spiralMatrix(matrix))