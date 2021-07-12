'''Nearest exit in the matrix other than enterance, we can use two algorithms dfs and bfs, but we should use bfs
in this scenario beacuse bfs has the tendency to givig us the shortest path and dfs do give tle in this case'''


#DFS
def nearestExit1(matrix,entrance):
    m = len(matrix)
    n = len(matrix[0])

    result = []

    def dfs(i,j,path):
        if [i,j]!= entrance and (i==0 or i==m-1 or j ==0 or j==n-1):
            result.append(path)
            return

        for x,y in [(0,1),(0,-1),(1,0),(-1,0)]:
            newx =i+x
            newy = j+y
            if 0<=newx<m and 0<=newy<n and matrix[newx][newy] == '.':
                matrix[newx][newy] = '+'
                dfs(newx,newy,path+1)
                matrix[newx][newy] = '.'
    dfs(entrance[0],entrance[1],0)
    return min(result) if result!=[] else -1





#BFS
from collections import deque
from sys import maxsize

def nearestExit2(matrix,entrance):

    m = len(matrix)
    n = len(matrix[0])
    visited = set((entrance[0],entrance[1]))
    q = deque([(entrance[0],entrance[1])])
    step = 0
    directions = [(0,1),(0,-1),(1,0),(-1,0)]
    while q:
        for i in range(len(q)):
            node = q.popleft()

            if node[0]==0 or node[0]==m-1 or node==[1]==0 or node[1]==n-1:
                if matrix[node[0]][node[1]] == '.' and [node[0],node[1]] != entrance:
                    return step


            for dirs in directions:
                d = (node[0]+dirs[0],node[1]+dirs[1])

                if d not in visited and 0<=d[0]<m and 0<=d[1]<n and matrix[d[0]][d[1]] == '.':
                    visited.add(d)
                    q.append(d)
        step+=1
    return -1

            



maze = maze = [["+","+","+"],[".",".","."],["+","+","+"]]
entrance = [1,0]
print(nearestExit2(maze,entrance))
