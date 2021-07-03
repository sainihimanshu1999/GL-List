'''Trapping rain water is a basic dp approach'''

def trappingWater(heights):
    n = len(heights)
    left = [0]*n
    right = [0]*n
    water = [0]*n

    maxLeft = 0
    maxRight = 0

    for i in range(n):
        maxLeft = max(maxLeft,heights[i])
        left[i] = maxLeft

    for i in range(n-1,-1,-1):
        maxRight = max(maxRight,heights[i])
        right[i] = maxRight

    for i in range(n):
        water[i] = min(left[i],right[i]) - heights[i]

    return sum(water)

height = [0,1,0,2,1,0,1,3,2,1,2,1]
print(trappingWater(height))