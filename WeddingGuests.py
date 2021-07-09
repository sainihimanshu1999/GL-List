'''This question is similar to meeting rooms 2, it can be done using two methods, one is normal iteration and other 
one is using heaps'''


#normal iterations

def wedding(start,end):
    all = [(s,1) for s in start] + [(e,-1) for e in end]

    all = sorted(all)

    num = 0

    maxChairs = 0

    for pos , t in all:
        num += t
        if maxChairs < num:
            maxChairs = num

    return maxChairs

#using heaps
from heapq import *

def wedding2(start,end):
    intervals = [[start[i],end[i]] for i in range(len(start))]
    
    intervals.sort(key=lambda x:x[0])

    heap = []
    chairs = 0

    for interval in intervals:
        if not heap or heap[0]>interval[0]:
            chairs +=1
            heappush(heap,interval[1])

        else:
            heappop(heap)
            heappush(heap,interval[1])
            
    return chairs


S = [1, 2, 6, 5, 3]
E = [5, 5, 7, 6, 8]
print(wedding2(S,E))