'''This is a basic dfs backtracking question, running time exponentially improves if we use memoization in this'''


def integerReplacement(n):
    memo = {1:0}

    def dfs(n,memo):
        if n in memo:
            return memo[n]

        if n%2==0:
            memo[n] = 1+dfs(n//2,memo)
            return memo[n]

        else:
            memo[n] = 1+min(dfs(n+1,memo),dfs(n-1,memo))
            return memo[n]


    return dfs(n,memo)