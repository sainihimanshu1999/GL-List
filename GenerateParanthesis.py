'''Generate paranthesis using recursion'''

def generateParanthesis(n):
    result = []
    def dfs(left,right,path,result):
        if left>right or left<0 or right<0:
            return
        
        if left == 0 and right == 0:
            result.append(path)
            return

        dfs(left-1,right,path+'(',result)
        dfs(left,right-1,path+')',result)


    dfs(n,n,'',result)
    return result



print(generateParanthesis(3))