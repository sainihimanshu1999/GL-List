'''Minimum cost path from left column to the right most column
'''
#still unsolved
def minCostPath(matrix):
    m = len(matrix)
    n = len(matrix[0])


    def dfs(i,j,path):
        print(path)
        if not i or not j:
            return False

        if j == n-1:
            #ath.append(matrix[i][j])
            cost = max(path)-min(path)
            print(cost)
            return cost

        return dfs(i,j+1,path.append(matrix[i][j+1])) or dfs(i+1,j+1,path.append(matrix[i+1][j])) or dfs(i-1,j+1,path.append(matrix[i][j+1]))

    result = []  
    for i in range(m):
        result.append( dfs(i,0,[matrix[i][0]]))
    #print(result)
    return min(result)

from heapq import *


def minCost2(nums):
    heap = [(row[0],i,0) for i,row in enumerate(nums)]
    heapify(heap)

    ans = float('-inf'),float('inf')

    right = max(row[0] for row in nums)

    while heap:
        left,i,j = heappop(heap)

        if right-left<ans[1]-ans[0]:
            ans = left,right

        if j+1 == len(nums[i]):
            return ans
        
        val = nums[i][j+1]
        right = max(right,val)

        heappush(heap,(val,i,j+1))



matrix = [[1,1,2],[2,2,1],[3,3,1]]
print(matrix)
print(minCost2(matrix))


