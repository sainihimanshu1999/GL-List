'''We use min heap in this question'''

from heapq import *

def skyLine(buildings):

    events = [(l,-h,r) for l,r,h in buildings]
    events += list((r,0,0) for _,r,_ in buildings)

    events.sort()

    heap = [(0,float('inf'))]
    result = [[0,0]]

    for l,h,r in events:
        
        while heap[0][1] <= l:
            heappop(heap)

        if h:
            heappush(heap,(h,r))

        if result[-1][1] != heap[0][1]:
            result += [[l,-heap[0][0]]]

    return result[1:]

buildings = [[2,9,10],[3,7,15],[5,12,12],[15,20,10],[19,24,8]]
print(skyLine(buildings))

