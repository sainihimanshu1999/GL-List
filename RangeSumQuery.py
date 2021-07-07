'''In this question we basically precompute matrix sum'''


def rectangle(matrix,row1,col1,row2,col2):
    m = len(matrix)
    n = len(matrix[0])

    dp = [[0]*(n+1) for _ in range(m+1)]

    for i in range(1,m+1):
        for j in range(1,n+1):
            dp[i][j] = matrix[i-1][j-1]+dp[i-1][j]+dp[i][j-1]+dp[i-1][j-1]


    row1,col1,row2,col2 = row1+1,col1+1,row2+1,col2+1

    return dp[row2][col2] - dp[row1-1][col2] -dp[row2][col1-1] - dp[row1-1][col1-1]



