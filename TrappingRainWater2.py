'''Trapping rain water in this 2D array, in this question we have to use mih heap and bfs. we will increment level one
by one and if we find any cell whose height is less than current level, means it can trap water. outside cells of 
matrix can't hold water'''

from heapq import *

def trappingRainWater(heights):
    if not heights or not heights[0]:
        return 0

    m = len(heights)
    n = len(heights[0])

    if m<3 or n<3:
        return 0


    heap = []

    for i in range(m):
        for j in range(n):
            if i == 0 or  i== m-1 or j == 0 or j==n-1:
                heappush(heap,(heights[i][j],i,j))
                heights[i][j] = -1


    level,water = 0,0

    while heap:
        h,x,y = heappop(heap)
        level = max(h,level)

        for i,j in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
            if 0<=i<=m-1 and 0<=j<=n-1 and heights[i][j] != -1:
                heappush(heap,(heights[i][j],i,j))

                if heights[i][j]<level:
                    water += level - heights[i][j]

            
                heights[i][j] = -1

    return water



heightMap = [[1,4,3,1,3,2],[3,2,1,3,2,4],[2,3,3,2,3,1]]
print(trappingRainWater(heightMap))